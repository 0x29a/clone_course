import logging
from celery import shared_task
from .utils import StudioApi

logger = logging.getLogger(__name__)


@shared_task
def clone_course(source_id, dest_id):
    """
    Celery task that calls the studio api for cloning course
    """
    logger.info("Task started for calling studio api for cloning course")
    api = StudioApi()
    api.clone_course_in_studio(source_id=source_id, dest_id=dest_id)
    logger.info("Task completed for calling studio api for cloning course")
