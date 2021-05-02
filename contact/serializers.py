from rest_framework import serializers
from contact.models import Contactme


class ContactmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactme
        fields = ('name', 'email', 'message')