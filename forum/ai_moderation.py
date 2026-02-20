from django.utils.timezone import now
from .models import tPost, tAiModerationLogs
import re
def moderate_post(post):

    content = post.sContent.lower()

    misleading_keywords = [
        "free money",
        "guaranteed profit",
        "click here to win",
        "buy now get rich",
        "investment with no risk"
    ]

    score = 0.0

    for word in misleading_keywords:
        pattern = re.escape(word)
        if re.search(pattern, content):
            score += 0.3

    # AI decision threshold
    if score >= 0.3:
        post.bIsFlagged = True
        post.dtFlaggedAt = now()
        post.fAiConfidenceScore = score
        post.iFlaggedBy = None
        post.save()

        # log AI moderation decision
        tAiModerationLogs.objects.create(
            iPostId=post,
            sAiLabel="Misleading Campaign",
            fConfidenceScore=score,
            jRawResponse={"reason": "Misleading keywords detected"}
        )