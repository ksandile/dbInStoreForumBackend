from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password

from .models import tPost, tComments, tLikes, tUsers
from .serializers import tPostSerializer, tCommentSerializer

# -----------------------
# Post ViewSet
# -----------------------
class tPostViewSet(viewsets.ModelViewSet):
    queryset = tPost.objects.all()
    serializer_class = tPostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user_id = request.data.get('user_id')
        post = self.get_object()

        if post.iUserId.iUserId == int(user_id):
            return Response({"error": "Cannot like your own post"}, status=status.HTTP_400_BAD_REQUEST)

        if tLikes.objects.filter(iPostId=post, iUserId__iUserId=user_id).exists():
            return Response({"error": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

        tLikes.objects.create(iPostId=post, iUserId=tUsers.objects.get(iUserId=user_id))
        return Response({"success": "Post liked"})

    @action(detail=True, methods=['patch'])
    def flag(self, request, pk=None):
        post = self.get_object()
        post.bIsFlagged = request.data.get("bIsFlagged", True)
        post.save()
        return Response({"success": "Post flagged"})

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        post = self.get_object()
        user_id = request.data.get('user_id')
        content = request.data.get('content')

        comment = tComments.objects.create(
            iPostId=post,
            iUserId=tUsers.objects.get(iUserId=user_id),
            sContent=content
        )
        serializer = tCommentSerializer(comment)
        return Response(serializer.data)


# -----------------------
# Register API
# -----------------------
@api_view(['POST'])
def register(request):
    name = request.data.get("name")
    email = request.data.get("email")
    password = request.data.get("password")

    if not name or not email or not password:
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    if tUsers.objects.filter(sEmail=email).exists():
        return Response({"error": "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)

    hashed_password = make_password(password)
    user = tUsers.objects.create(
        sUserName=name,
        sEmail=email,
        sPasswordHash=hashed_password,
        sRole="user"
    )
    return Response({
        "id": user.iUserId,
        "name": user.sUserName,
        "email": user.sEmail,
        "role": user.sRole
    }, status=status.HTTP_201_CREATED)


# -----------------------
# Login API
# -----------------------
@api_view(['POST'])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email and password required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = tUsers.objects.get(sEmail=email)
        if check_password(password, user.sPasswordHash):
            return Response({
                "id": user.iUserId,
                "name": user.sUserName,
                "email": user.sEmail,
                "role": user.sRole
            })
        else:
            return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
    except tUsers.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
