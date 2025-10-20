import React, { useEffect, useState } from "react";
import axios from "axios";
import NotesPanel from "../components/NotesPanel";
import VideoPlayer from "../components/VideoPlayer";

const API_BASE = "http://localhost:5000/api";

function ProjectPage({ projectId = 6, userId = 1 }) {
  const [project, setProject] = useState(null);
  const [resources, setResources] = useState([]);
  const [notes, setNotes] = useState([]);
  const [selectedVideo, setSelectedVideo] = useState(null);
  const [loading, setLoading] = useState(true);

  //Fetch project, resources, and notes
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [projectRes, resourceRes, notesRes] = await Promise.all([
          axios.get(`${API_BASE}/projects/${projectId}`),
          axios.get(`api/${API_BASE}/projects/${projectId}/resources`),
          axios.get(`${API_BASE}/projects/${projectId}/notes`),
        ]);

        setProject(projectRes.data);
        setResources(resourceRes.data);
        setNotes(notesRes.data);
        setSelectedVideo(resourceRes.data[0]); // auto-select first video
      } catch (error) {
        console.error("Error fetching project data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [projectId]);

  //  Add note
  const handleAddNote = async (noteData) => {
    try {
      const res = await axios.post(`${API_BASE}/projects/${projectId}/notes`, noteData);
      setNotes([...notes, res.data]); // update UI instantly
    } catch (error) {
      console.error("Error adding note:", error);
    }
  };

  if (loading) return <p>Loading project...</p>;
  if (!project) return <p>Project not found.</p>;

  return (
    <div className="project-page-container">
      {/* 🏗 Header */}
      <header className="project-header">
        <h1>{project.title}</h1>
        <p>{project.description}</p>
      </header>

      
      {/* {selectedVideo && (
        <VideoPlayer
          video={selectedVideo}
          resources={resources}
          onSelectVideo={setSelectedVideo}
        />
      )} */}

      <NotesPanel
        projectId={projectId}
        userId={userId}
        notes={notes}
        onAddNote={handleAddNote}
      />
    </div>
  );
};

export default ProjectPage;
