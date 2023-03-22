from typing import List
from models.alias import Alias
from loader.yaml_loader import YamlLoader


class AliasService:
    def fetch(self, path: str) -> List[Alias]:
        loaded_source = YamlLoader(path).load()

        return [
            Alias(name=key, command=value)
            for key, value in loaded_source["alias"].items()
        ]
