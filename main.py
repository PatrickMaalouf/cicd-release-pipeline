import os
import time

from app import app


def run() -> None:
    # Store start time for uptime calculations
    app.start_time = time.time()  # type: ignore[attr-defined]

    port = int(os.getenv("PORT", app.config.get("PORT", 8000)))
    app.run(host="0.0.0.0", port=port, debug=app.config.get("DEBUG", False))


if __name__ == "__main__":
    run()

