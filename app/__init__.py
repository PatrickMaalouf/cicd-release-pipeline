from flask import Flask
from dotenv import load_dotenv

from app.config import get_config
from app.core.response import ResponseFactory
from app.routes import register_routes


def create_app(config_name: str | None = None) -> Flask:
    """
    Application factory. Creates and configures the Flask app instance.
    """
    load_dotenv()

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(get_config(config_name))

    # Inject shared dependencies
    app.response_factory = ResponseFactory()  # type: ignore[attr-defined]

    # Register routes / blueprints
    register_routes(app)

    return app


app = create_app()
