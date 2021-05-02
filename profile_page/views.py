from rest_framework import viewsets,status
from django.db.models.functions import Concat
from django.db.models import Value
from rest_framework.response import Response

from profile_page.serializers import AboutSerializer
from profile_page.models import About


class AboutViewSet(viewsets.ViewSet):

    def list(self, request):
        data = About.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))

        serializer = AboutSerializer(data, many=True)
        return Response({'message': serializer.data}, status=status.HTTP_200_OK)




