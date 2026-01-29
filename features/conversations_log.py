from flask import Blueprint, render_template

conversations_log_bp = Blueprint('conversations_log', __name__)


@conversations_log_bp.route('')
def index():
    return render_template('conversations_log/index.html', title='Conversations')
