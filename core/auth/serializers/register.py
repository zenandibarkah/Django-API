from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    """
        Registration serializer for requests and user creation
    """
    # making sure the password is at least 8 characters long, and no longer than 128 and can't be read
    # by user
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name',
            'password'
        ]

    def create(self, validate_data):
        # Use create_user method we wrote earlier for UserManager to create new user
        return User.objects.create_user(**validate_data)