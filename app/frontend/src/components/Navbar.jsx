import React from "react";
import { useNavigate, useLocation } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();
  const location = useLocation();

  return (
    <nav style={styles.navbar}>
      
      <div
        style={styles.logo}
        onClick={() => navigate("/")}
      >
        StudySpace
      </div>

      
      <div style={styles.links}>
        <button
          onClick={() => navigate("/")}
          style={{
            ...styles.link,
            ...(location.pathname === "/projects" ? styles.activeLink : {}),
          }}
        >
          My Projects
        </button>
      </div>

      <div
        style={styles.avatar}
        onClick={() => navigate("/profile")}
      >
        <img
          src="https://i.pravatar.cc/40?img=5"
          alt="Profile"
          style={styles.avatarImg}
        />
      </div>
    </nav>
  );
};

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    backgroundColor: "#ffffff",
    padding: "10px 40px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.05)",
    position: "sticky",
    top: 0,
    zIndex: 1000,
  },
  logo: {
    fontSize: "1.5rem",
    fontWeight: "600",
    color: "#1e1e1e",
    cursor: "pointer",
  },
  links: {
    display: "flex",
    gap: "20px",
  },
  link: {
    background: "none",
    border: "none",
    color: "#444",
    fontSize: "1rem",
    cursor: "pointer",
    transition: "color 0.2s ease",
  },
  activeLink: {
    color: "#007bff",
    fontWeight: "600",
    textDecoration: "underline",
  },
  avatar: {
    width: "40px",
    height: "40px",
    borderRadius: "50%",
    overflow: "hidden",
    cursor: "pointer",
    border: "2px solid #eee",
    transition: "border 0.2s ease",
  },
  avatarImg: {
    width: "100%",
    height: "100%",
    objectFit: "cover",
  },
};

export default Navbar;
