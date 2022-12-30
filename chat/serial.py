from rest_framework.serializers import ModelSerializer
from chat.models import Message, Group

class MessageSerial(ModelSerializer):
	class Meta:
		model = Message
		fields = "__all__"

class GroupSerial(ModelSerializer):
	class Meta:
		model = Group
		fields = "__all__"
