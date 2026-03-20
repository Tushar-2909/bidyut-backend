from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

User = get_user_model()


# -----------------------------
# REGISTER SERIALIZER
# -----------------------------
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['role'] = 'user'  # 🔥 force user
        return User.objects.create_user(**validated_data)


# -----------------------------
# USER SERIALIZER (🔥 MISSING ONE)
# -----------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'role']


# -----------------------------
# CUSTOM LOGIN SERIALIZER
# -----------------------------
class CustomTokenSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        role = self.context['request'].data.get("role")

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        if role and user.role != role:
            raise serializers.ValidationError(f"You are not registered as {role}")

        data = super().validate({
            "username": user.email,
            "password": password
        })

        data["role"] = user.role

        return data