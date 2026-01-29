from flask import Blueprint, render_template

test_zone_bp = Blueprint('test_zone', __name__)


@test_zone_bp.route('')
def index():
    return render_template('test_zone/index.html', title='Test Zone')
