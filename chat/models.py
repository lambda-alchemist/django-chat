from django.contrib.auth.models import User
from django.db.models import (
	Model, ForeignKey, TextField, DateTimeField,
	DO_NOTHING, CASCADE
)

class Message(Model):
	user = ForeignKey(User, on_delete=CASCADE)
	text = TextField(max_length=127)
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)
	def __str__(self):
		user = self.user.username
		date = str(self.created_at)[:10]
		time = str(self.created_at)[11:19]
		return f"{user}, on {date}, at {time}"
