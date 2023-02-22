from django.test import TestCase
from rest_framework import status
from unittest.mock import MagicMock, patch

from ..views import CloneCourse
from ...tasks import clone_course
from ...utils import StudioApi


class TestCloneCourseViewSet(TestCase):

    def test_clone_course_view_set_post(self):
        """
        Test for calling the clone post api.
        """
        mock_task = MagicMock()
        mock_task.id = 'fake-task-id'
        data = {'source_id': 'abc', 'dest_id': 'def'}

        with patch('clone_course.apps.api.v1.views.clone_course.apply_async', return_value=mock_task):
            response = self.client.post('/api/v1/clone/clone/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'task_id': 'fake-task-id'})


    def test_status_view_set_get(self):
        """
        Test for calling status get api
        """
        task_id = "12345"
        mock_response = {
            'source_id': 'abc',
            'dest_id': 'def',
            'response': {'message': 'Course cloned successfully'}
        }
        with patch('clone_course.apps.api.v1.views.AsyncResult') as mock_async_result:
            mock_async_result.return_value.status = "SUCCESS"
            mock_async_result.return_value.result = mock_response
            response =self.client.get('/api/v1/clone/status/', kwargs={'task_id': task_id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "status": "SUCCESS",
            "source_id": "abc",
            "dest_id": "def",
            "response": {"message": "Course cloned successfully"}
        })

