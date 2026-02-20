import React, { useState } from "react";
import axios from "../api/axios";
import "../styles/PostCard.css";
import { IonIcon } from '@ionic/react';
import { heart, heartOutline } from 'ionicons/icons';

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
      await axios.patch(`/posts/${post.iPostId}/flag/`, {
        bIsFlagged: true,
        user_id: user.id
      });
      refreshPosts();
    } catch (err) {
      console.error(err);
      alert("Error flagging post");
    }
  };

  return (
    // <div className={`post-card ${post.bFlaggedMisleading ? "flagged" : ""}`}>
    //   <p>{post.sContent}</p>

    //   <div className="like-section" onClick={handleLike} style={{ cursor: 'pointer' }}>
    //     <IonIcon icon={heartOutline} style={{ fontSize: "24px", color: liked ? "red" : "black" }} />
    //     <span style={{ marginLeft: "8px" }}>{post.likes_count + (liked ? 1 : 0)}</span>
    //   </div>

    //   {user?.role === "moderator" && !post.bFlaggedMisleading && (
    //     <button onClick={handleFlag}>Flag Misleading</button>
    //   )}

    //   {post.bFlaggedMisleading && (
    //     <span className="flagged-text">Flagged by Moderator/AI</span>
    //   )}
    // </div>

    <div className={`post-card ${post.bFlaggedMisleading ? "flagged" : ""}`}>

      <p>{post.sContent}</p>

      <div className="like-section" onClick={handleLike}>
        <IonIcon
          icon={liked ? heart : heartOutline}
          style={{
            color: liked ? "red" : "black",
          }}
        />
        <span>{post.likes_count + (liked ? 1 : 0)}</span>
      </div>

      {user?.role === "moderator" && !post.bFlaggedMisleading && (
        <button onClick={handleFlag}>Flag Misleading</button>
      )}

      {post.bFlaggedMisleading && (
        <span className="flagged-text">Flagged by Moderator/AI</span>
      )}
    </div>
  );
};

export default PostCard; 