from rest_framework.serializers import ModelSerializer
from chat.models import Profile, Group, Message, Post, Reel

class ProfileSerial(ModelSerializer):
	class Meta:
		model = Profile
		fields = "__all__"

class GroupSerial(ModelSerializer):
	class Meta:
		model = Group
		fields = "__all__"

class MessageSerial(ModelSerializer):
	class Meta:
		model = Message
		fields = "__all__"

class PostSerial(ModelSerializer):
	class Meta:
		model = Post
		fields = "__all__"

class ReelSerial(ModelSerializer):
	class Meta:
		model = Reel
		fields = "__all__"
