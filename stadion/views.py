from .models import Club
from .serializer import ClubSerializer
from .task import celery_task
from rest_framework import generics


class ClubApiView(generics.ListAPIView):
    celery_task.delay()
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


    # return HttpResponse("<H1>salom</H1>")
