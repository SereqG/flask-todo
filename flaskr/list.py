from flask import Blueprint, render_template

bp = Blueprint("list", __name__, url_prefix="/")


@bp.route("/")
def list():
    to_do_items = [
        {"id": 1, "task_name": "Walk with the dog", "is_done": False, "time": "13:00"},
        {
            "id": 2,
            "task_name": "Study math for 40 minutes",
            "is_done": True,
            "time": "15:00",
        },
        {"id": 3, "task_name": "Clean my room", "is_done": False, "time": "12:00"},
        {"id": 4, "task_name": "Go to the gym", "is_done": False, "time": "18:00"},
    ]

    return render_template("list.html", items=to_do_items)
