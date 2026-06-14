import yaml
import os
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Backend:
    name: str
    url: str
    prefix: Optional[str] = None
    timeout: int = 30

def load_config(config_path: str = "config.yaml") -> List[Backend]:
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
        
    with open(config_path, "r") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML format in {config_path}: {e}")
            
    if not data or "backends" not in data:
        return []
        
    backends = []
    for entry in data["backends"]:
        if "name" not in entry:
            raise ValueError("Backend configuration missing required field: 'name'")
        if "url" not in entry:
            raise ValueError("Backend configuration missing required field: 'url'")
            
        backend = Backend(
            name=entry["name"],
            url=entry["url"],
            prefix=entry.get("prefix"),
            timeout=entry.get("timeout", 30)
        )
        backends.append(backend)
        
    return backends
