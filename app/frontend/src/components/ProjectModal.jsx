import { useState } from "react";

const ProjectModal = ({ onClose, onSubmit }) => {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.title.trim() || !formData.description.trim()) {
      alert("Please fill all fields");
      return;
    }
    onSubmit(formData);
  };

  return (
    <div style={styles.overlay}>
      <div style={styles.modal}>
        <h2 style={styles.title}>Create New Project</h2>

        <form onSubmit={handleSubmit} style={styles.form}>
          <input
            type="text"
            name="title"
            placeholder="Project Title"
            value={formData.title}
            onChange={handleChange}
            style={styles.input}
          />

          <textarea
            name="description"
            placeholder="Project Description"
            value={formData.description}
            onChange={handleChange}
            style={{ ...styles.input, height: "100px" }}
          />

          <div style={styles.buttonRow}>
            <button type="button" onClick={onClose} style={styles.cancel}>
              Cancel
            </button>
            <button type="submit" style={styles.create}>
              Create
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

const styles = {
  overlay: {
    position: "fixed",
    top: 0,
    left: 0,
    width: "100vw",
    height: "100vh",
    background: "rgba(0, 0, 0, 0.4)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    zIndex: 999,
  },
  modal: {
    background: "#fff",
    borderRadius: "12px",
    padding: "24px",
    width: "400px",
    boxShadow: "0 10px 20px rgba(0,0,0,0.2)",
  },
  title: {
    marginBottom: "16px",
    textAlign: "center",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "12px",
  },
  input: {
    padding: "10px",
    fontSize: "15px",
    borderRadius: "8px",
    border: "1px solid #ccc",
  },
  buttonRow: {
    display: "flex",
    justifyContent: "flex-end",
    gap: "10px",
    marginTop: "10px",
  },
  cancel: {
    padding: "8px 14px",
    background: "#eee",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
  },
  create: {
    padding: "8px 14px",
    background: "#007bff",
    border: "none",
    color: "#fff",
    borderRadius: "8px",
    cursor: "pointer",
  },
};

export default ProjectModal;
