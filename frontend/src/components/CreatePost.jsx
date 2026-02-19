import React, { useState } from "react";
import axios from "../api/axios";
import "../styles/CreatePost.css";

const CreatePost = ({ user, refreshPosts }) => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [campaignType, setCampaignType] = useState("Entrance Screen");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!user) return alert("Login to create a post");

    try {
      await axios.post("/posts/", {
        sTitle: title,
        sContent: content,
        campaign_type: campaignType,
        iUserId: user.id
      });
      setTitle("");
      setContent("");
      refreshPosts();
    } catch (err) {
      console.error(err);
      alert("Error creating post");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="create-post-page">
        <input
            type="text"
            placeholder="Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
        />
        <textarea
            placeholder="Content"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            required
        />
        <select value={campaignType} onChange={(e) => setCampaignType(e.target.value)}>
            <option>Entrance Screen</option>
            <option>End Cap</option>
            <option>Totem Display</option>
            <option>Aisle</option>
        </select>
        <button type="submit">Post</button>
    </form>

  );
};

export default CreatePost;
