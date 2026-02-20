from rest_framework import serializers
from .models import tPost, tComments, tLikes, tUsers


# POST SERIALIZER
class tPostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    bFlaggedMisleading = serializers.SerializerMethodField()
    iUserId = serializers.PrimaryKeyRelatedField(queryset=tUsers.objects.all())
    iFlaggedBy = serializers.PrimaryKeyRelatedField(queryset=tUsers.objects.all(), allow_null=True)

    class Meta:
        model = tPost
        fields = [
            'iPostId',
            # 'sTitle',
            'sContent',
            'iUserId',
            'bIsFlagged',
            'bFlaggedMisleading',
            'iFlaggedBy',
            'dtFlaggedAt',
            'likes_count',
            'dtCreatedAt'
        ]

    def get_likes_count(self, obj):
        return tLikes.objects.filter(iPostId=obj).count()

    def get_bFlaggedMisleading(self, obj):
        return bool(obj.bIsFlagged)  # ensures True/False, never None


# COMMENT SERIALIZER
class tCommentSerializer(serializers.ModelSerializer):

    iUserId = serializers.PrimaryKeyRelatedField(
        queryset=tUsers.objects.all()
    )

    iPostId = serializers.PrimaryKeyRelatedField(
        queryset=tPost.objects.all()
    )

    class Meta:
        model = tComments
        fields = [
            'iCommentId',
            'iPostId',
            'iUserId',
            'sContent',
            'dtCreatedAt'
        ]


# LIKE SERIALIZER
class tLikeSerializer(serializers.ModelSerializer):

    iUserId = serializers.PrimaryKeyRelatedField(
        queryset=tUsers.objects.all()
    )

    iPostId = serializers.PrimaryKeyRelatedField(
        queryset=tPost.objects.all()
    )

    class Meta:
        model = tLikes
        fields = [
            'iLikeId',
            'iPostId',
            'iUserId',
            'dtCreatedAt'
        ]
