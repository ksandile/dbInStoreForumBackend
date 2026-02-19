import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import PostCard from "../components/PostCard";
import CreatePost from "../components/CreatePost";

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
    <div>
      <h2>Campaign Discussions</h2>
      {user && <CreatePost user={user} refreshPosts={fetchPosts} />}
      {posts.length === 0 ? <p>No posts yet</p> :
        posts.map(post => (
          <PostCard key={post.id} post={post} user={user} refreshPosts={fetchPosts} />
        ))
      }
    </div>
  );
};

export default Dashboard;
