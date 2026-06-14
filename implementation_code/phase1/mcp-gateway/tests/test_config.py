import pytest
import os
import yaml
from mcp_gateway.config import load_config, Backend

def test_load_valid_config(tmp_path):
    config_file = tmp_path / "config.yaml"
    valid_yaml = """
    backends:
      - name: test_echo
        url: http://localhost:8080
      - name: test_mock
        url: http://localhost:8081
        prefix: mock
        timeout: 15
    """
    config_file.write_text(valid_yaml)
    
    backends = load_config(str(config_file))
    assert len(backends) == 2
    
    assert backends[0].name == "test_echo"
    assert backends[0].url == "http://localhost:8080"
    assert backends[0].prefix is None
    assert backends[0].timeout == 30  # default
    
    assert backends[1].name == "test_mock"
    assert backends[1].prefix == "mock"
    assert backends[1].timeout == 15

def test_missing_config_file():
    with pytest.raises(FileNotFoundError, match="Configuration file not found"):
        load_config("nonexistent_config.yaml")

def test_missing_required_field_name(tmp_path):
    config_file = tmp_path / "config.yaml"
    invalid_yaml = """
    backends:
      - url: http://localhost:8080
    """
    config_file.write_text(invalid_yaml)
    
    with pytest.raises(ValueError, match="missing required field: 'name'"):
        load_config(str(config_file))

def test_missing_required_field_url(tmp_path):
    config_file = tmp_path / "config.yaml"
    invalid_yaml = """
    backends:
      - name: test_echo
    """
    config_file.write_text(invalid_yaml)
    
    with pytest.raises(ValueError, match="missing required field: 'url'"):
        load_config(str(config_file))

def test_invalid_yaml_format(tmp_path):
    config_file = tmp_path / "config.yaml"
    invalid_yaml = "backends: [unclosed_bracket"
    config_file.write_text(invalid_yaml)
    
    with pytest.raises(ValueError, match="Invalid YAML format"):
        load_config(str(config_file))
