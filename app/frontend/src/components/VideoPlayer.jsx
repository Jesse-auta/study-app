import React, { useState, useEffect } from "react";

const VideoPlayer = ({ videos }) => {
  const [currentVideo, setCurrentVideo] = useState(null);

  useEffect(() => {
    if (videos && videos.length > 0) {
      setCurrentVideo(videos[0]);
    }
  }, [videos]);

  const getEmbedUrl = (url) => {
    if (!url) return null;
    const match = url.match(/(?:v=|be\/)([a-zA-Z0-9_-]{11})/);
    return match ? `https://www.youtube.com/embed/${match[1]}` : null;
  };

  if (!currentVideo) {
    return <p>No videos available for this project.</p>;
  }

  return (
    <div className="video-player">
      <h3>{currentVideo.title}</h3>
      <iframe
        src={getEmbedUrl(currentVideo.url)}
        title={currentVideo.title}
        frameBorder="0"
        allowFullScreen
      />
      <div className="video-thumbnails">
        {videos.map((vid) => (
          <img
            key={vid.id}
            src={vid.thumbnail}
            alt={vid.title}
            style={{
              width: "120px",
              cursor: "pointer",
              margin: "10px",
              border: currentVideo.id === vid.id ? "2px solid blue" : "none",
            }}
            onClick={() => setCurrentVideo(vid)}
          />
        ))}
      </div>
    </div>
  );
};

export default VideoPlayer;

