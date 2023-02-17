from unittest import mock
from django.test import TestCase
from django.core.exceptions import ImproperlyConfigured
from ..utils import StudioApi


class TestStudioApi(TestCase):

    @mock.patch('clone_course.apps.api.utils.OAuthAPIClient.request')
    def test_clone_course_in_studio_success(self, mock_request):
        """
        Test that clone_course_in_studio function makes a post request to
        the studio API with the correct course data, given valid source and
        destination course ids.
        """
        api = StudioApi()

        source_id = 'source-course-id'
        dest_id = 'destination-course-id'

        api.clone_course_in_studio(source_id, dest_id)

        expected_data = {
            'source_course_id': source_id,
            'destination_course_id': dest_id,
        }
        mock_request.assert_called_once_with(
            'post',
            'http://example.com/api/v1/course_runs/clone/',
            json=expected_data,
        )

    def test_generate_data_for_studio_api_success(self):
        """
        Test generate_data_for_studio_api function to ensure it generates data
        correctly based on the source and destination course ids.
        """
        api = StudioApi()

        source_id = 'source-course-id'
        dest_id = 'destination-course-id'

        data = api.generate_data_for_studio_api(source_id, dest_id)

        expected_data = {
            'source_course_id': source_id,
            'destination_course_id': dest_id,
        }
        self.assertEqual(data, expected_data)

    def test_generate_data_for_studio_api_source_id_missing(self):
        """
        Test that generate_data_for_studio_api function raises an
        ImproperlyConfigured error when source course id is not provided.
        """
        api = StudioApi()

        with self.assertRaises(ImproperlyConfigured):
            api.generate_data_for_studio_api(None, 'destination-course-id')

    def test_generate_data_for_studio_api_dest_id_missing(self):
        """
        Test that generate_data_for_studio_api function raises an
        ImproperlyConfigured error when destination course id is not provided.
        """
        api = StudioApi()

        with self.assertRaises(ImproperlyConfigured):
            api.generate_data_for_studio_api('source-course-id', None)

    def test_make_studio_url_success(self):
        """
        Test that _make_studio_url function returns a valid URL, given a
        valid path and STUDIO_ROOT_URL environment variable.
        """
        api = StudioApi()

        path = 'foo/bar/'

        with self.settings(STUDIO_ROOT_URL='http://studio.example.com/'):
            url = api._make_studio_url(path)

        expected_url = 'http://studio.example.com/api/v1/foo/bar/'
        self.assertEqual(url, expected_url)

    def test_make_studio_url_missing_studio_root_url(self):
        """
        Test that _make_studio_url function raises an ImproperlyConfigured error
        when STUDIO_ROOT_URL environment variable is not set.
        """
        api = StudioApi()

        path = 'foo/bar/'

        with self.settings(STUDIO_ROOT_URL=""):
            with self.assertRaises(ImproperlyConfigured):
                api._make_studio_url(path)
