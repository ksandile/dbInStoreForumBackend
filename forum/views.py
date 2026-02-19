from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import tPost, tComments, tLikes, tUsers

from .serializers import tPostSerializer, tCommentSerializer, tLikeSerializer

class tPostViewSet(viewsets.ModelViewSet):
    queryset = tPost.objects.all()
    serializer_class = tPostSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user_id = request.data.get('user_id')
        post = self.get_object()
        
        # Prevent liking own post
        if post.iUserId.id == user_id:
            return Response({"error": "Cannot like your own post"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Prevent duplicate likes
        if tLikes.objects.filter(iPostId=post, iUserId__id=user_id).exists():
            return Response({"error": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)
        
        tLikes.objects.create(iPostId=post, iUserId=tUsers.objects.get(id=user_id))
        return Response({"success": "Post liked"})

    @action(detail=True, methods=['patch'])
    def flag(self, request, pk=None):
        post = self.get_object()
        post.flagged_misleading = request.data.get("flagged_misleading", True)
        post.save()
        return Response({"success": "Post flagged"})

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        post = self.get_object()
        user_id = request.data.get('user_id')
        content = request.data.get('content')
        
        comment = tComments.objects.create(
            post_id=post,
            user_id=tUsers.objects.get(id=user_id),
            content=content
        )
        serializer = tCommentSerializer(comment)
        return Response(serializer.data)
