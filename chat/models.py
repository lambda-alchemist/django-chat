from django.contrib.auth.models import User
from django.db.models import (
	Model, ForeignKey,
	TextField, DateTimeField,
	ManyToManyField, ImageField,
	DO_NOTHING, CASCADE,
)

class Profile(Model):
	user = ForeignKey(User, on_delete=CASCADE)
	picture = ImageField(upload_to='chat/profile/picture')
	created_at = created_at = DateTimeField(auto_now_add=True)
	def __str__(self):
		return f"{self.user.username}'s profile, created on {str(self.created_at)[:10]}"

class Reel(Model):
	poster = ForeignKey(Profile, on_delete=CASCADE)
	caption = TextField(max_length=128)
	image = ImageField
	created_at = DateTimeField(auto_now_add=True)
	def __str__(self):
		return f""

class Message(Model):
	sender = ForeignKey(User, on_delete=CASCADE, related_name='sent_messages')
	reciever = ForeignKey(User, null=True,on_delete=DO_NOTHING, related_name='recieved_messages')
	group = ForeignKey('chat.Group', null=True, on_delete=CASCADE)
	text = TextField(max_length=8192)
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		user = self.sender.username
		date = str(self.created_at)[:10]
		time = str(self.created_at)[11:19]
		return f"{user}, on {date}, at {time}"


class Group(Model):
	desc = TextField(max_length=127)
	members = ManyToManyField(User, through='chat.Membership')
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

class Membership(Model):
	user  = ForeignKey(User,  on_delete=DO_NOTHING, related_name='person')
	group = ForeignKey(Group, on_delete=DO_NOTHING, related_name='club')
