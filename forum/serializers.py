from rest_framework import serializers
from .models import tPost, tComments, tLikes, tUsers


# POST SERIALIZER
class tPostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    bFlaggedMisleading = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    vibe = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = tPost
        fields = [
            'iPostId',
            'sContent',
            'iUserId',
            'bIsFlagged',
            'bFlaggedMisleading',
            'likes_count',
            'comment_count',
            "fAiConfidenceScore",
            'liked_by_user',
            'vibe',
            'dtCreatedAt'
        ]
    def get_liked_by_user(self, obj):
        user = self.context.get('user') 
        if user:
            return tLikes.objects.filter(iPostId=obj.iPostId, iUserId__iUserId=user.iUserId).exists()
        return False
    
    def get_bFlaggedMisleading(self, obj):
        return obj.bIsFlagged

    def get_likes_count(self, obj):
        return tLikes.objects.filter(iPostId=obj.iPostId).count()

    def get_comment_count(self, obj):
        return tComments.objects.filter(iPostId=obj.iPostId).count()

    def get_vibe(self, obj):
        comments = tComments.objects.filter(iPostId=obj.iPostId)

        toxic_words = ["stupid","nonsense","hate","trash"]
        humour_words = ["lol","haha","funny"]
        constructive_words = ["suggest","improve","recommend"]
        informative_words = ["because","therefore","fact"]

        score = {
            "Toxic":0,
            "Humorous":0,
            "Constructive":0,
            "Informative":0
        }

        for c in comments:
            text = c.sContent.lower()
            for w in toxic_words:
                if w in text: score["Toxic"]+=1
            for w in humour_words:
                if w in text: score["Humorous"]+=1
            for w in constructive_words:
                if w in text: score["Constructive"]+=1
            for w in informative_words:
                if w in text: score["Informative"]+=1

        return max(score, key=score.get) if comments.exists() else "Neutral"


# COMMENT SERIALIZER
class tCommentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="iUserId.sUserName", read_only=True)

    vibe = serializers.SerializerMethodField()

    class Meta:
        model = tComments
        fields = [
            'iCommentId',
            'iPostId',
            'iUserId',
            'sContent',
            'dtCreatedAt',
            'name',   
            'vibe'   
        ]

    def get_vibe(self, obj):
        toxic_words = ["stupid","nonsense","hate","trash"]
        humour_words = ["lol","haha","funny"]
        constructive_words = ["suggest","improve","recommend"]
        informative_words = ["because","therefore","fact"]

        score = {
            "Toxic": 0,
            "Humorous": 0,
            "Constructive": 0,
            "Informative": 0
        }

        text = obj.sContent.lower()
        for w in toxic_words:
            if w in text:
                score["Toxic"] += 1
        for w in humour_words:
            if w in text:
                score["Humorous"] += 1
        for w in constructive_words:
            if w in text:
                score["Constructive"] += 1
        for w in informative_words:
            if w in text:
                score["Informative"] += 1

        return max(score, key=score.get) if text else "Neutral"
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
