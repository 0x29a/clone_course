import logging
from celery.result import AsyncResult
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..tasks import clone_course

logger = logging.getLogger(__name__)


class CloneCourse(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def clone(self, request):
        """
        Calls the celery task for cloning course and returns the task id
        """
        source_id = request.data.get("source_id")
        dest_id = request.data.get("dest_id")
        task = clone_course.apply_async(args=(source_id, dest_id))
        task_id = task.id
        return Response({"task_id": task_id})
    
    @action(detail=False, methods=['get'])
    def status(self, request):
        """
        Queries the task status
        """
        task_id = request.query_params.get("task_id")
        task = AsyncResult(task_id)
        response = task.result
        return Response({
            "status": task.status,
            "source_id": response.get('source_id', ""),
            "dest_id": response.get('dest_id', ""),
            "response": response.get('response', {}),
        })
