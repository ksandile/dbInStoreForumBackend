import React, { useState } from "react";
import axios from "../api/axios";

const PostCard = ({ post, user, refreshPosts }) => {
  const [liked, setLiked] = useState(false);

  const handleLike = async () => {
    if (!user) return alert("Login to like posts!");
    if (post.iUserId === user.id) return alert("Cannot like your own post");

    try {
        await axios.post(`/posts/${post.iPostId}/like/`, { user_id: user.id });
      setLiked(true);
      refreshPosts();
    } catch (err) {
      console.error(err);
      alert("Error liking post");
    }
  };

  const handleFlag = async () => {
    if (user.role !== "moderator") return alert("Only moderators can flag");
    try {
        await axios.patch(`/posts/${post.iPostId}/flag/`, { bIsFlagged: true });
      refreshPosts();
    } catch (err) {
      console.error(err);
      alert("Error flagging post");
    }
  };

  return (
    <div className="post-card">
      <h3>{post.sTitle}</h3>
      <p>{post.sContent}</p>
      <p><b>Type:</b> {post.campaign_type}</p>
      <p><b>Likes:</b> {post.likes_count}</p>
      <button onClick={handleLike} disabled={liked}>Like</button>
      {user?.role === "moderator" && !post.bFlaggedMisleading && (
        <button onClick={handleFlag}>Flag Misleading</button>
      )}
      {post.bFlaggedMisleading && <span style={{color:"red"}}>Flagged by Moderator/AI</span>}
    </div>
  );
};

export default PostCard;
