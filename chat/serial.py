from rest_framework.serializers import ModelSerializer
from chat.models import Profile, Group, Message, Post, Reel

class ProfileSerial(ModelSerializer):
	class Meta:
		model = Profile
		fields = [
			"user",
			"created_at",
			"updated_at"
		]

class ProfilePictureSerial(ModelSerializer):
	class Meta:
		model = Profile
		fields = "picture"

class GroupSerial(ModelSerializer):
	class Meta:
		model = Group
		fields = "__all__"

class GroupPictureSerial(ModelSerializer):
	class Meta:
		model = Group
		fields = "image"

class MessageSerial(ModelSerializer):
	class Meta:
		model = Message
		fields = "__all__"

class PostSerial(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			"poster",
			"text",
			"created_at",
		]

class PostPictureSerial(ModelSerializer):
	class Meta:
		model = Post
		fileds = "image"

class ReelSerial(ModelSerializer):
	class Meta:
		model = Reel
		fields = [
			"reeler",
			"caption",
			"created_at",
		]

class ReelPictureSerial(ModelSerializer):
	class Meta:
		model = Reel
		fileds = "image"

