from flask import Blueprint, jsonify, request
from app.models.note import Note
from app.models.project import Project
from app.extensions import db

notes_bp = Blueprint("notes", __name__)

# Get all notes for a project
@notes_bp.route("/api/projects/<int:project_id>/notes", methods=["GET"])
def get_notes(project_id):
    project = Project.query.get_or_404(project_id)
    notes = [note.to_dict() for note in project.notes]
    return jsonify(notes), 200


@notes_bp.route("/api/projects/<int:project_id>/notes", methods=["POST"])
def add_note(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    user_id = data.get("user_id")

    if not data or "content" not in data:
        return jsonify({"error": "Content is required"}), 400

    new_note = Note(content=data["content"], project=project, user_id=user_id)
    db.session.add(new_note)
    db.session.commit()
    print(new_note)

    return jsonify(new_note.to_dict()), 201


@notes_bp.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    data = request.get_json()

    if not data or not data.get("content"):
        return jsonify({"error": "Content is required"}), 400

    note.content = data["content"]
    db.session.commit()

    return jsonify(note.to_dict()), 200


@notes_bp.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note deleted"}), 200


