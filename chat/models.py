from django.contrib.auth.models import User
from django.db.models import (
	Model, ForeignKey, TextField, TimeField,
	DO_NOTHING, CASCADE
)

class ChatMessage(Model):
	user = ForeignKey(User, on_delete=DO_NOTHING)
	text = TextField(max_length=127)
	