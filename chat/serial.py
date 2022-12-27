from rest_framework.serializers import ModelSerializer
from chat.models import ChatMessage

class MessageSerial(ModelSerializer):
	class Meta:
		model = ChatMessage
		fields = "__all__"

