import React, { useState, useEffect, useCallback } from "react";
import axios from "../api/axios";
import "../styles/PostCard.css";
import { IonIcon } from '@ionic/react';
import { heart, heartOutline, flagOutline } from 'ionicons/icons';

const PostCard = ({ post, user, refreshPosts }) => {
  const [comments, setComments] = useState([]);
  const [showComments, setShowComments] = useState(false);
  const [newComment, setNewComment] = useState("");
  const [liked, setLiked] = useState(false); 

  const vibeEmoji = {
    Toxic: "😡",
    Humorous: "😂",
    Constructive: "🛠",
    Informative: "📘",
    Neutral: "🙂"
  };

  const isLiked = () => {
    return liked || post.liked_by_user;
  };

  const fetchComments = useCallback(async () => {
    try {
      const res = await axios.get(`/posts/${post.iPostId}/comment/`);
      setComments(res.data);
    } catch (err) {
      console.log(err);
    }
  }, [post.iPostId]);

  useEffect(() => {
    if (showComments) fetchComments();
  }, [showComments, fetchComments]);

  useEffect(() => {
    setLiked(post.liked_by_user);
    // console.log(`Post ID: ${post.iPostId}, liked_by_user: ${post.liked_by_user}`);
  }, [post.liked_by_user, post.iPostId]);

  const handleComment = async () => {
    if (!newComment.trim()) return;
    try {
      await axios.post(`/posts/${post.iPostId}/comment/`, {
        user_id: user.id,
        content: newComment
      });
      setNewComment("");
      fetchComments();
      refreshPosts();
    } catch (err) {
      console.error(err);
    }
  };

  const handleLike = async () => {
    if (isLiked()) return; 

    try {
      setLiked(true); 
      await axios.post(`/posts/${post.iPostId}/like/`, { user_id: user.id });
      refreshPosts(); 
    } catch (err) {
      console.error(err);
      setLiked(post.liked_by_user); 
    }
  };

  return (
    <div className={`post-card ${post.bFlaggedMisleading ? "flagged" : ""}`}>
      <div className="post-content">
        <p>{post.sContent}</p>
        {post.bIsFlagged && post.fAiConfidenceScore && (
          <div className="ai-flag-info">
            ⚠️ Flagged by AI (Confidence: {post.fAiConfidenceScore.toFixed(2)})
          </div>
        )}
      </div>

      <div className="post-vibe">
        {vibeEmoji[post.vibe]} <span>{post.vibe}</span>
      </div>

      <div className="post-actions">
        <div className="like-section" onClick={handleLike}>
          <IonIcon icon={isLiked() ? heart : heartOutline} />
          <span>{post.likes_count + (!post.liked_by_user && liked ? 1 : 0)}</span>
          <div style={{ color: isLiked() ? "red" : "black" }}>Like</div>
        </div>

        <div className="like-section" onClick={() => setShowComments(!showComments)}>
          <span>{post.comment_count} Comments</span>
        </div>
      </div>

      {user?.role === "moderator" && !post.bFlaggedMisleading && (
        <IonIcon
          icon={flagOutline}
          size="large"
          color="danger"
          className="flag-icon"
          onClick={async () => {
            try {
              await axios.patch(`/posts/${post.iPostId}/flag/`, {
                user_id: user.id,
                bIsFlagged: true
              });
              refreshPosts();
            } catch (err) {
              console.error(err);
            }
          }}
        />
      )}

      {showComments && (
        <div className="comments-box">
          {comments.map(c => (
            <div key={c.iCommentId} className="comment">
              <div className="comment-header">{c.name}</div>
              <div className="comment-body">
                {c.sContent} {vibeEmoji[c.vibe]}
              </div>
            </div>
          ))}

          {user && (
            <>
              <input
                value={newComment}
                onChange={(e) => setNewComment(e.target.value)}
                placeholder="Write comment..."
              />
              <button onClick={handleComment}>Send</button>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default PostCard;