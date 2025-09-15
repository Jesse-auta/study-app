from flask import Blueprint, jsonify, request
from app.models.project import Project
from app.extensions import db

project_bp = Blueprint("projects", __name__)

@project_bp.route("/api/projects", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return jsonify([p.to_dict() for p in projects])


@project_bp.route("/api/projects", methods=["POST"])
def create_projects():
    data = request.get_json()

    title = data["title"]
    if not title:
        return jsonify({"Error": "title is required"})
    
    description = data.get("description")

    project = Project(title=title, description=description)

    db.session.add(project)
    db.session.commit()


    return jsonify(project.to_dict()), 201

@project_bp.route("/api/projects/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    project = Project.query.get(project_id)
    data = request.get_json()
    print(data)
    if data.get("title"):
        project.title = data["title"]

    if data.get("description"): 
        project.description = data["description"]

    db.session.commit()

    return jsonify(project.to_dict()), 201

@project_bp.route("/api/projects/<int:project_id>", methods=["GET"])
def get_project(project_id):
    project = Project.query.get(project_id)

    return jsonify(project.to_dict()), 201


@project_bp.route("/api/projects/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    project = Project.query.get(project_id)

    db.session.delete(project)
    db.session.commit()

    return jsonify({"message" : "Project deleted"})
