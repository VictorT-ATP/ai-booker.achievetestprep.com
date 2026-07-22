
from flask import Blueprint, abort, current_app, request
from urllib.parse import urlparse
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .svc_connector import get_status_details
from .elevenlabs_connector import get_agents
# Initialize Limiter with application-wide default limits
limiter = Limiter(
    get_remote_address, # Identifies clients by their IP address
    app=current_app,
    default_limits=["200 per day", "50 per hour"], # Applied globally to all routes
    storage_uri="memory://", # Default in-memory backend
)

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

@api_bp.before_request
def access_validation():
    ALLOWED_HOSTS = str.split(current_app.config['ALLOWED_HOSTS'], ',')
    if urlparse(request.base_url).hostname not in ALLOWED_HOSTS:
        abort(403, description="Forbidden: Invalid Client")

@api_bp.route("/status-details")
@api_bp.route("/status-details/{agent_id}")
def get_status_details_endpoint(agent_id=None):
    return {'what': 'yes'} #get_status_details(agent_id)


@api_bp.route("/status")
def get_status_endpoint():
    return {'what': 'yes'}

@api_bp.route("/agents")
def get_agents_endpoint():
    return get_agents()