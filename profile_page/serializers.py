from rest_framework import serializers
from .models import About


class AboutSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=256)
    class Meta:
        model = About
        fields = ('full_name', 'job', 'description')
