import json
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey
from .models import ChatSession, Message
from .serializers import MessageSerializer


class HomePageView(TemplateView):
    template_name = 'seoai/home.html'


class UserMessageView(APIView):
    permission_classes = [HasAPIKey]

    def post(self, request):
        # Extract the nested JSON string and parse it
        data_str = request.data.get('value')
        if data_str:
            try:
                data = json.loads(data_str.replace("'", '"'))  # Handle single quotes
            except json.JSONDecodeError:
                return Response({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Now pass the parsed data to the serializer
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            session, created = ChatSession.objects.get_or_create(
                session_id=serializer.validated_data['session_id'],
                defaults={'flow_id': serializer.validated_data['flow_id']}
            )
            Message.objects.create(
                session=session,
                message_type='user',
                content=serializer.validated_data['content']
            )
            return Response({"status": "User message saved"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BotMessageView(APIView):
    permission_classes = [HasAPIKey]

    def post(self, request):
        # Extract the nested JSON string and parse it
        data_str = request.data.get('value')
        if data_str:
            try:
                data = json.loads(data_str.replace("'", '"'))  # Handle single quotes
            except json.JSONDecodeError:
                return Response({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Now pass the parsed data to the serializer
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            session, created = ChatSession.objects.get_or_create(
                session_id=serializer.validated_data['session_id'],
                defaults={'flow_id': serializer.validated_data['flow_id']}
            )
            Message.objects.create(
                session=session,
                message_type='bot',
                content=serializer.validated_data['content']
            )
            return Response({"status": "Bot message saved"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoryMessageView(APIView):
    permission_classes = [HasAPIKey]

    def post(self, request):
        # Extract the nested JSON string and parse it
        data_str = request.data.get('value')
        if data_str:
            try:
                data = json.loads(data_str.replace("'", '"'))  # Handle single quotes
            except json.JSONDecodeError:
                return Response({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Now pass the parsed data to the serializer
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            session, created = ChatSession.objects.get_or_create(
                session_id=serializer.validated_data['session_id'],
                defaults={'flow_id': serializer.validated_data['flow_id']}
            )
            Message.objects.create(
                session=session,
                message_type='history',
                content=serializer.validated_data['content']
            )
            return Response({"status": "History message saved"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
