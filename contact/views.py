from rest_framework import viewsets,status
from rest_framework.response import Response

from contact.serializers import ContactmeSerializer



class ContactmeViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        data =request.data
        serializer = ContactmeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': serializer.data}, status=201)
        else:
            return Response({'message': serializer.data}, status=400)
