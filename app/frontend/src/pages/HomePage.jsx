import { useState, useEffect } from "react";
import { fetchProjects, createProject } from "../api/projectAPI";
import ProjectModal from "../components/ProjectModal";
import { useNavigate } from "react-router-dom";

function HomePage() {
  const [projects, setProjects] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  useEffect(() => {
    async function loadProjects() {
        try {
            const data = await fetchProjects()
            setProjects(data)
            console.log(data)
        }catch(err) {
            console.error(err)
        }
    }
    loadProjects();
  }, []);

  const handleViewProject = (projectId) => {
    navigate(`/project/${projectId}`)
  }

  const handleCreateProject = async (formData) => {
    try {
        const newProject = await createProject(formData)
        setProjects((prev) => [...prev, newProject])
        setShowModal(false)
    }catch (err) {
        console.error(err)
        alert("Error creating project");
    }
  }



   return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1>Your Projects</h1>
        <button style={styles.newBtn} onClick={() => setShowModal(true)}>
          + New Project
        </button>
      </header>

      <div style={styles.list}>
        {projects.map((project) => (
          <div key={project.id} style={styles.card}>
            <h3>{project.title}</h3>
            <p>{project.description}</p>
            <button style={styles.openBtn} onClick={() => handleViewProject(project.id)}>Open Project</button>
          </div>
        ))}
      </div>

      {showModal && (
        <ProjectModal
          onClose={() => setShowModal(false)}
          onSubmit={handleCreateProject}
        />
      )}
    </div>
    
  );

}

const styles = {
    container: { padding: "2rem" },
    header: {
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
    },
    openBtn: {
        marginTop: "40px"
    },

    newBtn: {
        padding: "8px 16px",
        background: "#007bff",
        border: "none",
        color: "white",
        borderRadius: "8px",
        cursor: "pointer",
        
    },
    list: {
        marginTop: "2rem",
        display: "grid",
        gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
        gap: "1rem",
    },
    card: {
        padding: "1rem",
        borderRadius: "8px",
        background: "#f9f9f9",
        boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
    },
    };

export default HomePage;



