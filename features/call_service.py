from flask import Blueprint, render_template

call_service_bp = Blueprint('call_service', __name__)


@call_service_bp.route('')
def index():
    return render_template('call_service/index.html', title='Call Service')
