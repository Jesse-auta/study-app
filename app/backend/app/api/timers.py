from flask import jsonify, request, Blueprint
from app.models.timer import Timer
from app.extensions import db
from datetime import datetime, timezone, timedelta


timers_bp = Blueprint("timers", __name__)
@timers_bp.route("/timers", methods=["POST"])
def create_timer():
    data = request.get_json()
    user_id = data.get("user_id")
    duration = data.get("duration_seconds")

    new_timer = Timer(user_id=user_id, duration_seconds=duration)
    db.session.add(new_timer)
    db.session.commit()

    return jsonify({
        "id": new_timer.id,
        "user_id": new_timer.user_id,
        "start_time": new_timer.start_time,
        "duration_seconds": new_timer.duration_seconds,
        "is_active": new_timer.is_active
    }), 201


@timers_bp.route("/timers/<int:timer_id>", methods=["GET"])
def get_timer(timer_id):
    timer = Timer.query.get_or_404(timer_id)

    remaining = None
    if timer.duration_seconds:
        end_time = timer.start_time + timedelta(seconds=timer.duration_seconds)
        remaining = (end_time - datetime.now(timezone.utc)).total_seconds()
        remaining = max(0, remaining)

    return jsonify({
        "id": timer.id,
        "user_id": timer.user_id,
        "start_time": timer.start_time,
        "duration_seconds": timer.duration_seconds,
        "is_active": timer.is_active,
        "remaining_seconds": remaining
    })


@timers_bp.route("/timers", methods=["GET"])
def list_timers():
    user_id = request.args.get("user_id")  # ?user_id=1
    query = Timer.query
    if user_id:
        query = query.filter_by(user_id=user_id)

    timers = query.all()
    results = []
    for timer in timers:
        remaining = None
        if timer.duration_seconds:
            end_time = timer.start_time + timedelta(seconds=timer.duration_seconds)
            remaining = (end_time - datetime.now(timezone.utc)).total_seconds()
            remaining = max(0, remaining)

        results.append({
            "id": timer.id,
            "user_id": timer.user_id,
            "start_time": timer.start_time,
            "duration_seconds": timer.duration_seconds,
            "is_active": timer.is_active,
            "remaining_seconds": remaining
        })

    return jsonify(results)


@timers_bp.route("/timers/<int:timer_id>/stop", methods=["PUT"])
def stop_timer(timer_id):
    timer = Timer.query.get_or_404(timer_id)
    timer.is_active = False
    db.session.commit()

    return jsonify({
        "message": "Timer stopped",
        "id": timer.id,
        "is_active": timer.is_active
    })


@timers_bp.route("/timers/<int:timer_id>", methods=["DELETE"])
def delete_timer(timer_id):
    timer = Timer.query.get_or_404(timer_id)
    db.session.delete(timer)
    db.session.commit()
    return jsonify({"message": "Timer deleted"})
