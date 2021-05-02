from rest_framework import viewsets,status
from rest_framework.response import Response

from projects.serializers import ProjectSerializer
from projects.models import Project


class ProjectViewSet(viewsets.ViewSet):

    def list(self, request):
        data = Project.objects.all()
        serializer = ProjectSerializer(data, many=True)
        return Response({'message': serializer.data}, status=status.HTTP_200_OK)
