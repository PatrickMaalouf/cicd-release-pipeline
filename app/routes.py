from __future__ import annotations

import time
from typing import Any, Dict

from flask import Blueprint, Flask, current_app


def register_routes(app: Flask) -> None:
    """
    Route registration with explicit wiring to keep responsibilities clear.
    """
    api = Blueprint("api", __name__)

    @api.route("/", methods=["GET"])
    def root() -> tuple[Dict[str, Any], int]:
        response_factory = current_app.response_factory  # type: ignore[attr-defined]

        payload = {
            "app": current_app.config.get("APP_NAME"),
            "environment": current_app.config.get("ENVIRONMENT"),
        }
        return response_factory.success(data=payload, message="Root endpoint")

    @api.route("/health", methods=["GET"])
    def health() -> tuple[Dict[str, Any], int]:
        response_factory = current_app.response_factory  # type: ignore[attr-defined]
        payload = {"healthy": True}
        return response_factory.success(data=payload, message="Health check OK")

    @api.route("/status", methods=["GET"])
    def status() -> tuple[Dict[str, Any], int]:
        response_factory = current_app.response_factory  # type: ignore[attr-defined]

        start_time: float = getattr(current_app, "start_time", time.time())
        uptime_seconds = int(time.time() - start_time)

        payload = {
            "uptime_seconds": uptime_seconds,
            "environment": current_app.config.get("ENVIRONMENT"),
        }
        return response_factory.success(data=payload, message="Service status")

    app.register_blueprint(api)

