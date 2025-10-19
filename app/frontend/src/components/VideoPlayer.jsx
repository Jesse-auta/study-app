const VideoPlayer = ({ video, resources, onSelectVideo }) => {
  return (
    <div className="video-player">
      <iframe
        src={`https://www.youtube.com/embed/${video.url.split("v=")[1]}`}
        title={video.title}
        allowFullScreen
      />
      <div className="video-list">
        {resources.map((res) => (
          <button
            key={res.id}
            onClick={() => onSelectVideo(res)}
            className={res.id === video.id ? "active" : ""}
          >
            {res.title}
          </button>
        ))}
      </div>
    </div>
  );
};

export default VideoPlayer;
