import mimetypes
from flask import Flask, render_template
from dotenv import load_dotenv
from logging.config import dictConfig
import logging
import os

load_dotenv()
mimetypes.add_type('text/javascript', '.js')

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

app = Flask(__name__)

def create_app():
    app.jinja_env.variable_start_string = '[['
    app.jinja_env.variable_end_string = ']]'
    app.logger.setLevel(logging.DEBUG if os.getenv(
        "FLASK_DEBUG", "true").lower() == "true" else logging.INFO)
    app.config['ALLOWED_HOSTS'] = os.getenv("ALLOWED_HOSTS")
    return app

# Dashboard
@app.route('/')
def index():
    data = {
        'title': 'Dashboard'
    }
    return render_template('dashboard/index.html', **data)

# features: Dialer Service
@app.route('/call_service')
def call_service():
    data = {
        'title': 'Dialer Service'
    }
    return render_template('call_service/index.html', **data)

# features: Test Zone
@app.route('/test_zone')
def test_zone():
    data = {
        'title': 'Test Zone'
    }
    return render_template('test_zone/index.html', **data)

# features: Conversation Log
@app.route('/conversations_log')
def conversations_log():
    data = {
        'title': 'Conversations'
    }
    return render_template('conversations_log/index.html', **data)

# features: Statistics
@app.route('/statistics')
def statistics():
    data = {
        'title': 'Statistics'
    }
    return render_template('statistics/index.html', **data)

# features: Settings
@app.route('/settings')
def settings():
    data = {
        'title': 'Settings'
    }
    return render_template('settings/index.html', **data)

if __name__ == "__main__":
    main_app = create_app()
    main_app.run(port=5000, debug=True)
