import json
from flask import Blueprint, render_template, make_response
from .info import PRE_PATH, PROJECT_NAME, STATIC_DIR, VIEWS_DIR

site = Blueprint("site", PROJECT_NAME, template_folder=VIEWS_DIR)


@site.route("/", methods=["GET"])
def root():
    return render_template("root.html", pre_path=PRE_PATH)


@site.route("/_model/model", methods=["GET"])
def _model_model():
    MODEL_PATH = STATIC_DIR / "model" / "model.json"
    model = json.load(MODEL_PATH.open("r"))
    return model