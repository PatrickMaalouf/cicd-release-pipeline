import os
from dataclasses import dataclass


@dataclass
class BaseConfig:
    APP_NAME: str = os.getenv("APP_NAME", "Flask Railway API")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    PORT: int = int(os.getenv("PORT", "8000"))


@dataclass
class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True


@dataclass
class ProductionConfig(BaseConfig):
    DEBUG: bool = False


def get_config(config_name: str | None) -> type[BaseConfig]:
    """
    Simple config resolver based on name or ENVIRONMENT variable.
    """
    if not config_name:
        env = os.getenv("ENVIRONMENT", "development").lower()
    else:
        env = config_name.lower()

    if env == "production":
        return ProductionConfig

    return DevelopmentConfig

