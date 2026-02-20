import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import PostCard from "../components/PostCard";
import CreatePost from "../components/CreatePost";
import "../styles/Dashboard.css";

const Dashboard = ({ user }) => {
  const [posts, setPosts] = useState([]);

  const fetchPosts = async () => {
    try {
      const res = await axios.get("/posts/");
      setPosts(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div className="dashboard-page">
      <h2 className="dashboard-header">Campaign Discussions</h2>

      {/* Centered CreatePost Section */}
      {user && (
        <div className="create-post-container">
          <CreatePost user={user} refreshPosts={fetchPosts} />
        </div>
      )}

      {/* Centered Posts */}
      <div className="posts-container">
        {posts.length === 0 ? (
          <p>No posts yet</p>
        ) : (
          posts.map(post => (
            <PostCard
              key={post.iPostId}
              post={post}
              user={user}
              refreshPosts={fetchPosts}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default Dashboard;