from rest_framework import serializers
from .models import tPost, tComments, tLikes, tUsers

class tPostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    bFlaggedMisleading = serializers.BooleanField(source="flagged_misleading")

    class Meta:
        model = tPost
        fields = ['id', 'sTitle', 'sContent', 'campaign_type', 'iUserId', 'likes_count', 'bFlaggedMisleading']

    def get_likes_count(self, obj):
        return tLikes.objects.filter(iPostId=obj.id).count()


class tCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = tComments
        fields = ['id', 'post_id', 'user_id', 'content']


class tLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = tLikes
        fields = ['id', 'iPostId', 'iUserId']
