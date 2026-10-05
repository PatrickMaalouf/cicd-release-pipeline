from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class ApiResponse:
    data: Any = field(default_factory=dict)
    status: int = 200
    message: str = "Success"

    def to_dict(self) -> Mapping[str, Any]:
        return asdict(self)


class ResponseFactory:
    """
    Responsible for creating standardized API responses.
    Keeps response shape consistent across the application (Single Responsibility).
    """

    def success(self, data: Any | None = None, message: str = "Success", status_code: int = 200) -> tuple[Mapping[str, Any], int]:
        body = ApiResponse(
            data=data if data is not None else {},
            status=status_code,
            message=message,
        )
        return body.to_dict(), status_code

    def error(self, message: str, status_code: int = 400, data: Any | None = None) -> tuple[Mapping[str, Any], int]:
        body = ApiResponse(
            data=data if data is not None else {},
            status=status_code,
            message=message,
        )
        return body.to_dict(), status_code

