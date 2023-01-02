from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models import (
	Model,
	TextField,
	CharField,
	ImageField,
	DateTimeField,
	ForeignKey,
	ManyToManyField,
	CASCADE,
	DO_NOTHING)

class Profile(Model):
	user = ForeignKey(User, on_delete=CASCADE)
	picture = ImageField(upload_to='media/profiles/', null=True)
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		name = self.user.username
		date = str(self.created_at)[:10]
		return f"{name}'s profile, created on {date}"

class Group(Model):
	title = CharField(max_length=127, unique=True, default='blankName')
	desc = TextField(max_length=255, blank=True)
	picture = ImageField(upload_to='media/groups/', null=True)
	members = ManyToManyField(User, through='chat.Membership')
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

class Membership(Model):
	user  = ForeignKey(User,  on_delete=DO_NOTHING, related_name='person')
	group = ForeignKey(Group, on_delete=DO_NOTHING, related_name='club')
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		user = self.user.username
		club = self.group.title
		date = str(self.created_at)[:10]
		time = str(self.created_at)[11:19]
		return f"The user {user} joined {club}, on {date}, at {time}"

class Message(Model):
	user = ForeignKey(User, on_delete=CASCADE, related_name='sent_messages')
	reciever = ForeignKey(User, null=True, blank=True, on_delete=DO_NOTHING, related_name='recieved_messages')
	group = ForeignKey(Group, null=True, blank=True, on_delete=CASCADE)
	text = TextField(max_length=8192)
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		user = self.user.username
		date = str(self.created_at)[:10]
		time = str(self.created_at)[11:19]
		return f"Sent by {user}, on {date}, at {time}"

class Post(Model):
	user = ForeignKey(User, on_delete=CASCADE)
	text = TextField(max_length=8192)
	picture = ImageField(upload_to='media/posts/')
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		name = self.user.username
		date = str(self.created_at)[:10]
		time = str(self.created_at)[11:19]
		return f"{name}'s post, on {date}, at {time}"

class Reel(Model):
	user = ForeignKey(User, on_delete=CASCADE)
	caption = TextField(max_length=128)
	picture = ImageField(upload_to='media/reels/', null=True)
	created_at = DateTimeField(auto_now_add=True)

	def __str__(self):
		name = self.user.username
		time = str(self.created_at)[11:19]
		return f"{name}'s profile, created on {time}"
