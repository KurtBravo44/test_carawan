from rest_framework import generics, permissions

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]