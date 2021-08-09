from rest_framework import serializers
from .models import Images
from django.contrib.auth.hashers import make_password
from appentousapp.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        email = attrs.get("email")
        if User.objects.filter(email=email):
            raise serializers.ValidationError("Email already exists.")
        return super().validate(attrs)

    def create(self, attrs):
        attrs["password"] = make_password(attrs.get("password"))
        user = User.objects.create(**attrs)
        return user


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source="id", read_only=True)
    user_name = serializers.CharField(source="username", read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["user_id", "user_type", "user_name", "images"]

    def get_images(self, obj):
        imgs = Images.objects.filter(user_id=obj.id)
        serializer = ImageSerializer(imgs, many=True)
        return serializer.data
