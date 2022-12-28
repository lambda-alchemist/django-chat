from rest_framework.serializers import ModelSerializer
from chat.models import Message

class MessageSerial(ModelSerializer):
	class Meta:
		model = Message
		fields = "__all__"

