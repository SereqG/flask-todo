from flask import Blueprint, render_template

bp = Blueprint("list", __name__, url_prefix="/")


@bp.route("/")
def list():
    return render_template("list.html")
