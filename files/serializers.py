from rest_framework import serializers
from .models import File

class FileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    file = serializers.FileField()
    uploaded_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return File.objects.create(**validated_data)