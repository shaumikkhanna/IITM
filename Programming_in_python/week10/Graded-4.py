
class UserLoginInfo:

	def __init__(self, username, password):
		self.UserName = username
		self.old_passwords = [password]

	def RetrievePassword(self):
		return self.old_passwords[-1]

	@staticmethod
	def is_valid_password(password: str) -> bool:
		truth = []
		# Length must be greater than 7
		truth.append(len(password) > 7)
		# First character must be a letter and in uppercase
		truth.append(password[0].isupper())
		# All characters are either a number or letter
		truth.append(password.isalnum())

		return all(truth)

	def ChangePassword(self, new_password):
		# Check if password is reused
		if new_password in self.old_passwords:
			return 'Password already used'

		# Check if password is invalid
		if not UserLoginInfo.is_valid_password(new_password):
			return 'Invalid password'

		# Update password
		self.old_passwords.append(new_password)
		return 'Password updated successfully'

	def Login(self, username, password):
		if username == self.UserName and password == self.RetrievePassword():
			return f'Welcome {self.UserName}'
		else:
			return 'Username or Password incorrect'

