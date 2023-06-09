import yaml
from typing import Any


class PathNotValidError(Exception):
    pass


class YamlLoader:
    def __init__(self, path: str, encording: str) -> None:
        self.path = path
        self.encording = encording

    def load(self) -> Any:
        if not self.__is_valid():
            raise PathNotValidError(f"ファイル名が[yaml, yml]形式ではありません. path={self.path}")

        with open(self.path, mode="r", encording=self.encording) as file:
            return yaml.safe_load(file)

    def __is_valid(self) -> bool:
        return self.path.endswith(".yaml") or self.path.endswith(".yml")
