from flask import Blueprint, render_template, request, redirect, url_for
from .forms import ResponseForm
from .models import Response
from . import db

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ResponseForm()
    if form.validate_on_submit():
        response = Response(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(response)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('form.html', form=form)
