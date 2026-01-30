from flask import Flask
from dotenv import load_dotenv
from logging.config import dictConfig
import logging
import os

load_dotenv()

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s > %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "log/app.log",
                "maxBytes": 1000000,
                "backupCount": 10,
                "formatter": "default",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)


def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.DEBUG if os.getenv(
        "FLASK_DEBUG", "true").lower() == "true" else logging.INFO)

    # Register

    # features: Dashboard
    from features.dashboard import dashboard_bp

    app.register_blueprint(dashboard_bp, url_prefix='/')

    # features: Administration
    from features.admin import admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # features: Call Service
    from features.call_service import call_service_bp
    app.register_blueprint(call_service_bp, url_prefix='/call_service')

    # features: Test Zone
    from features.test_zone import test_zone_bp
    app.register_blueprint(test_zone_bp, url_prefix='/test_zone')

    # features: Calls Log
    from features.conversations_log import conversations_log_bp
    app.register_blueprint(conversations_log_bp,
                           url_prefix='/conversations_log')
    # features: Statistics
    from features.statistics import statistics_bp
    app.register_blueprint(statistics_bp, url_prefix='/statistics')
    # features: Settings
    from features.settings import settings_bp
    app.register_blueprint(settings_bp, url_prefix='/settings')

    return app


if __name__ == "__main__":
    main_app = create_app()
    main_app.run(port=5000)
