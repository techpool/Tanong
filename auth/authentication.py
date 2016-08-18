from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class CustomBackend(object):
	def authenticate(self, email=None, password=None):
		try:
			user = User.objects.get(email=email)
			user_password = user.password
			pwd_valid = check_password(password, user_password)

			if pwd_valid:
				return user
			else:
				return None
		except User.DoesNotExist:
			return None

	def get_user(self, email_id):
		try:
			return User.objects.get(pk=email_id)
		except User.DoesNotExist:
			return None