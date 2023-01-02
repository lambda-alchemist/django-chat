from rest_framework.serializers import ModelSerializer, ImageField
from chat.models import Profile, Group, Message, Post, Reel

class ProfileSerial(ModelSerializer):
	class Meta:
		model = Profile
		fields = [
			"user",
			"created_at",
			"updated_at"
		]

class GroupSerial(ModelSerializer):
	class Meta:
		model = Group
		fields = [
			"title",
			"desc",
			"created_at",
			"updated_at"
		]

class MessageSerial(ModelSerializer):
	class Meta:
		model = Message
		fields = "__all__"

class PostSerial(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			"user",
			"text",
			"created_at",
		]

class ReelSerial(ModelSerializer):
	class Meta:
		model = Reel
		fields = [
			"user",
			"caption",
			"created_at",
		]

class ProfilePictureSerial(ModelSerializer):
	class Meta:
		model = Profile
		fields = ["picture"]

class GroupPictureSerial(ModelSerializer):
	class Meta:
		model = Group
		fields = ["picture"]
	picture = ImageField()
	def save(self):
		picture = self.validated_data['image']
		picture.name = str(self.context['request'].user.id) + '.jpg'
		picture.save()

class PostPictureSerial(ModelSerializer):
	class Meta:
		model = Post
		fileds = ["picture"]

class ReelPictureSerial(ModelSerializer):
	class Meta:
		model = Reel
		fileds = ["picture"]
