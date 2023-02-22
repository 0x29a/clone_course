# Add check for valid source and dest course id
# Call studio api for clone_course
from urllib.parse import parse_qsl, urlencode, urljoin
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from edx_rest_api_client.client import OAuthAPIClient
from requests.exceptions import HTTPError


class StudioApi:
    def __init__(self):
        self._api = OAuthAPIClient(
            settings.OAUTH2_PROVIDER_URL,
            settings.BACKEND_SERVICE_EDX_OAUTH2_KEY,
            settings.BACKEND_SERVICE_EDX_OAUTH2_SECRET,
        )

    def _make_studio_url(self, path):
        if hasattr(settings, 'STUDIO_ROOT_URL'):
            studio_rool_url = settings.STUDIO_ROOT_URL
        else:
            studio_rool_url = None

        if not studio_rool_url:
            error_msg = "Set the STUDIO_ROOT_URL env variable!"
            raise ImproperlyConfigured(error_msg)
    
        return urljoin(studio_rool_url, 'api/v1/' + path)

    def _request(self, method, path, **kwargs):
        url = self._make_studio_url(path)
        response = self._api.request(method, url, **kwargs)
        try:
            response.raise_for_status()
        except HTTPError as exc:
            # Add a content field as extra debugging info for logging above us. This used to be automatically added
            # by slumber, but now with requests module, we need to manually add it.
            exc.content = response.content
            raise exc
        return response.json()
    
    def generate_data_for_studio_api(self, source_id, dest_id):
        if not source_id:
            # add type check
            error_msg = "Source course id should be provided"
            raise ImproperlyConfigured(error_msg)
        if not dest_id:
            # add type check
            error_msg = "Destination course id should be provided"
            raise ImproperlyConfigured(error_msg)
        data = {
            'source_course_id': source_id,
            'destination_course_id': dest_id,
        }

        return data
    
    def clone_course_in_studio(self, source_id, dest_id):
        data = self.generate_data_for_studio_api(source_id, dest_id)
        response = self._request('post', 'course_runs/clone/', json=data)
        return response
