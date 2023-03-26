from dataclasses import dataclass


@dataclass
class Alias:
    """Alias"""

    name: str
    command: str

    def to_string(self) -> str:
        return f"alias {self.name}='{self.command}'"
