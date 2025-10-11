from flask import Blueprint, request, jsonify
from app.models.resource import Resource
from app.models.project import Project
from app.extensions import db
from app.utils.youtube import generate_youtube_thumbnail


resources_bp = Blueprint("resources", __name__)


@resources_bp.route("/projects/<int:project_id>/resources", methods=["POST"])
def create_resource(project_id):
    data = request.get_json()
    errors = []

    if not data.get('title'):
        errors.append("Title is required.")
    elif len(data['title']) < 3:
        errors.append("Title must be at least 3 characters long.")

    if not data.get('url'):
        errors.append("URL is required.")

    if not data.get('user_id'):
        errors.append("User ID is required.")

    if errors:
        return jsonify({"errors": errors}), 400

    try:
        user_id = int(data.get("user_id"))
    except ValueError:
        return jsonify({'error': 'user_id must be an integer'}), 400

    
    url = data.get("url")
    title = data.get("title")
    thumbnail_url = generate_youtube_thumbnail(url)  # Generate thumbnail
    resource_type = data.get("resource_type", "video")

    project = Project.query.get_or_404(project_id)

    resource = Resource(
        project_id=project.id,
        user_id=user_id,
        title=title,
        url=url,
        thumbnail_url=thumbnail_url,
        resource_type=resource_type
    )

    db.session.add(resource)
    db.session.commit()

    return jsonify({
        "message": "Resource created successfully",
        "resource": {
            "id": resource.id,
            "title": resource.title,
            "url": resource.url,
            "thumbnail_url": resource.thumbnail_url,
            "type": resource.resource_type
        }
    }), 201


@resources_bp.route("/projects/<int:project_id>/resources", methods=["GET"])
def list_resources(project_id):
    project = Project.query.get_or_404(project_id)
    resources = Resource.query.filter_by(project_id=project.id).all()

    return jsonify([
        {
            "id": r.id,
            "title": r.title,
            "url": r.url,
            "thumbnail_url": r.thumbnail_url,
            "type": r.resource_type,
            "uploader": r.user.username if r.user else None
        }
        for r in resources
    ])


@resources_bp.route("/resources/<int:resource_id>", methods=["GET"])
def get_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    return jsonify({
        "id": resource.id,
        "title": resource.title,
        "url": resource.url,
        "thumbnail_url": resource.thumbnail_url,
        "type": resource.resource_type,
        "project": resource.project.title,
        "uploader": resource.user.username if resource.user else None
    })


@resources_bp.route("/resources/<int:resource_id>", methods=["DELETE"])
def delete_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    db.session.delete(resource)
    db.session.commit()

    return jsonify({"message": "Resource deleted successfully"})
