from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    session_id = serializers.CharField(max_length=255)
    content = serializers.CharField()
    flow_id = serializers.CharField(max_length=255)
