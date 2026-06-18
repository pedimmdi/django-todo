from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAnonymous
from drf_spectacular.utils import extend_schema, OpenApiExample


class UserRegistrationView(APIView):
    permission_classes = [IsAnonymous]
    @extend_schema(
        tags=["Accounts"],
        summary="Register new user",
        description="Create a new user account using email and password.",
        request=UserRegistrationSerializer,
        responses={201: UserRegistrationSerializer},
        examples=[
            OpenApiExample(
                "Register Example",
                value={
                    "email": "john@example.com",
                    "password": "StrongPassword123"
                },
                request_only=True,
            ),
        ],
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(
        tags=["Profiles"],
        summary="Get current profile",
        description="Retrieve profile information of authenticated user.",
        responses={200: ProfileSerializer}
    )
    def get(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    
    @extend_schema(
        tags=["Profiles"],
        summary="Update current profile",
        description="Update profile information of authenticated user.",
        request=ProfileSerializer,
        responses={200: ProfileSerializer},
        examples=[
            OpenApiExample(
                "Profile Example",
                value={
                    "first_name": "John",
                    "last_name": "Doe",
                    "bio": "Backend Developer"
                },
                request_only=True,
            )
        ],
    )
    def put(self, request):
        profile = request.user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
