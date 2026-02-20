from django.db import models

# Users table
class tUsers(models.Model):
    iUserId = models.AutoField(primary_key=True)
    sUserName = models.CharField(max_length=150)
    sEmail = models.EmailField(unique=True)
    sPasswordHash = models.CharField(max_length=256)
    sRole = models.CharField(max_length=50, default="user")
    bIsActive = models.BooleanField(default=True)
    dtCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sUserName

# Posts table
class tPost(models.Model):
    iPostId = models.AutoField(primary_key=True)
    iUserId = models.ForeignKey(tUsers, on_delete=models.CASCADE)
    sContent = models.TextField()
    bIsFlagged = models.BooleanField(default=False)
    iFlaggedBy = models.ForeignKey(
        tUsers,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='flagged_posts'
    )

    dtFlaggedAt = models.DateTimeField(null=True, blank=True)

    fAiConfidenceScore = models.FloatField(default=0.0)
    dtCreatedAt = models.DateTimeField(auto_now_add=True)
    fAiConfidenceScore = models.FloatField(default=0.0)
    dtCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.iPostId} by User {self.iUserId}"

# Comments table
class tComments(models.Model):
    iCommentId = models.AutoField(primary_key=True)
    iPostId = models.ForeignKey(tPost, on_delete=models.CASCADE)
    iUserId = models.ForeignKey(tUsers, on_delete=models.CASCADE)
    sContent = models.TextField()
    dtCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.iCommentId} on Post {self.iPostId}"

# Likes table
class tLikes(models.Model):
    iLikeId = models.AutoField(primary_key=True)
    iPostId = models.ForeignKey(tPost, on_delete=models.CASCADE)
    iUserId = models.ForeignKey(tUsers, on_delete=models.CASCADE)
    dtCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Like {self.iLikeId} on Post {self.iPostId}"

# AI Moderation Logs table
class tAiModerationLogs(models.Model):
    iLogId = models.AutoField(primary_key=True)
    iPostId = models.ForeignKey(tPost, on_delete=models.CASCADE)
    sAiLabel = models.CharField(max_length=200)
    fConfidenceScore = models.FloatField(default=0.0)
    jRawResponse = models.JSONField()
    bReviewed = models.BooleanField(default=False)
    dtCreatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Log {self.iLogId} for Post {self.iPostId}"
