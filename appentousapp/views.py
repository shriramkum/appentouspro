from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Images
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"status": status.HTTP_201_CREATED, "message": "success", "data": serializer.data}
            return Response(data)
        else:
            data = {"status": status.HTTP_400_BAD_REQUEST, "message": "Fail", "data": serializer.errors}
            return Response(data)


class Image_view(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        data = {"status": status.HTTP_200_OK, "message": "retrived success", "data": serializer.data}
        return Response(data)

    def post(self, request):
        images = request.data.getlist("image", [])
        for img in images:
            data = Images(user_id=request.user.id, image=img)
            data.save()
        serializer = UserSerializer(request.user)
        data = {"status": status.HTTP_201_CREATED, "message": "upload success", "data": serializer.data}
        return Response(data)
