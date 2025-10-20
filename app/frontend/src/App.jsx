import { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ProjectModal from "./components/ProjectModal";
import HomePage from "./pages/HomePage";
import ProjectPage from "./pages/ProjectPage";


function App() {
    
    
  return (
    <Router>
      <Routes>
        {/* Pass the openModal function down so HomePage can trigger it */}
        {/* <Route path="/" element={<HomePage/>} /> */}
        <Route path="/" element={<ProjectPage/>} />
        
      </Routes>
    </Router>
  );

}
export default App;
