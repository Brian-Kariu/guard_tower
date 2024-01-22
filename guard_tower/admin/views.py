"""Admin views"""
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required
from guard_tower.utils import flash_errors
from guard_tower.admin.forms import CreateAppForm
from guard_tower.admin.models import App
from guard_tower.user.models import User
from guard_tower.database import db

blueprint = Blueprint("admin", __name__, url_prefix="/admin",static_folder="../static")

@blueprint.route("/")
@login_required
def dashboards():
    """Manage admin dashboards"""
    apps = db.session.query(App).order_by(App.id).all()
    return render_template("admin/dashboard.html", apps=apps)

@blueprint.route("/apps/", methods=['POST', 'GET'])
@blueprint.route("/apps/<int:app_id>", methods=['POST', 'GET', 'DELETE'])
@login_required
def apps(app_id=None):
    """Manage Applications"""
    form = CreateAppForm(request.form)
    if request.method == "POST" and app_id is None:
        if form.validate_on_submit():
            try:
                App.create(name=form.name.data)
                db.session.commit()
                flash("App created successfully!", "success")
            except Exception as e:
                db.session.rollback()
                flash(str(e), "error")  # Better error handling
            return redirect(url_for("public.home"))
        else:
            flash_errors(form)

    if request.method == "GET" and app_id is None:
        return render_template("admin/create_app.html", apps=apps, form=form)
    if request.method == "GET" and app_id is not None:
        app = db.session.query(App).filter_by(id=app_id).first()
        return render_template("admin/view_app.html", app=app)
    if request.method == "POST" and app_id is not None:
        app = db.session.query(App).filter_by(id=app_id).first()
        return render_template("admin/create_app.html", app=app)
