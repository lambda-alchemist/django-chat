from django.contrib.auth.models import User
from django.db.models import (
	Model, ForeignKey,
	TextField, DateTimeField,
	ManyToManyField, ManyToManyRel,
	DO_NOTHING, CASCADE,
)

class Message(Model):
	sender = ForeignKey(User, on_delete=CASCADE, related_name='sent_messages')
	reciever = ForeignKey(User, null=True,on_delete=DO_NOTHING, related_name='recieved_messages')
	group = ForeignKey('chat.Group', null=True, on_delete=CASCADE)
	text = TextField(max_length=127)
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
