from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserProfileSerializer


class APIMyProfile(APIView):

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(
            user, many=False, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = UserProfileSerializer(
            user, many=False, context={'request': request},
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        user = request.user
        serializer = UserProfileSerializer(
            user, data=request.data, partial=True,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
