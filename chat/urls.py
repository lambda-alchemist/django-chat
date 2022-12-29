from django.urls import path
from chat.views import (
	IndexPage, LoginPage,
	SignupPage, LogoutView,
	check_user, #get_msg,
)

urlpatterns = [
	path('index/', IndexPage.as_view(), name='index'),
	path('login/', LoginPage.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('register/', SignupPage.as_view(), name='signup'),
	path('hx-check-user/', check_user, name='user-check'),
	# path('hx-get-msg/', get_msg, name='msg-getter'),
]
