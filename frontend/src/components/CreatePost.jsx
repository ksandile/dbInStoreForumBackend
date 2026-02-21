import React, { useState } from "react";
import axios from "../api/axios";
import "../styles/CreatePost.css";

const CreatePost = ({ user, refreshPosts }) => {
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!user) return alert("Login to create a post");

    try {
      await axios.post("/posts/", {
        sContent: content,
        iUserId: user.id
      });
      setContent("");
      refreshPosts();
    } catch (err) {
      console.error(err);
      alert("Error creating post");
    }
  };

  return (
    <div className="create-post-wrapper">
      <h2 className="create-post-header">Start a Discussion</h2>
      <form onSubmit={handleSubmit} className="create-post-form">
        <textarea
          placeholder="Share your thoughts..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
        />
        <button type="submit">Post</button>
      </form>
    </div>
  );
};

export default CreatePost;