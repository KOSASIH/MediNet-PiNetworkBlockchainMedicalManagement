# medinet/config.py

import os
import json
from typing import Dict, Any

class Config:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = config_file
        self.config: Dict[str, Any] = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        if not os.path.exists(self.config_file):
            raise MediNetError("Config file not found")

        with open(self.config_file, "r") as f:
            return json.load(f)

    def get(self, key: str) -> Any:
        return self.config.get(key)

    def set(self, key: str, value: Any) -> None:
        self.config[key] = value
        self.save_config()

    def save_config(self) -> None:
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

    def __repr__(self) -> str:
        return f"Config(config_file={self.config_file})"

# Example config.json file
# {
#     "database": {
#         "host": "localhost",
#         "port": 5432,
#         "username": "medinet",
#         "password": "password"
#     },
#     "api": {
#         "host": "0.0.0.0",
#         "port": 5000
#     }
# }
