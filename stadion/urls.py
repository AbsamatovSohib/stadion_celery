from django.urls import path
# from stadion.task import celery_task
from .views import ClubApiView

urlpatterns = [
    path("", ClubApiView.as_view())
]
