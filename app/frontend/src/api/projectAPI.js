
import api from "./axiosConfig";



export async function fetchProjects() {
  const res = await api.get("/api/projects");
  return res.data;
}

export async function createProject(data) {
  const res = await api.post("/api/projects", data);
  return res.data;
}
