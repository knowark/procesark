from typing import Dict, Any


Config = Dict[str, Any]


BASE: Config = {
    "mode": "BASE",
    "port": 6291,
    "strategies": ["base"],
    "strategy": {},
    "tenancy": {
        "dsn": ""
    },
    "zones": {
        "default": {
            "dsn": ""
        }
    }
}

DEVELOPMENT_CONFIG: Config = {**BASE, **{
    "mode": "DEV",
    "factory": "CheckFactory",
    "strategies": ["base", "check"],
    "tenancy": {
        "dsn": "postgresql://procesark:procesark@localhost/procesark"
    },
    "zones": {
        "default": {
            "dsn": "postgresql://procesark:procesark@localhost/procesark"
        }
    }
}}

PRODUCTION_CONFIG: Config = {**BASE, **{
    "mode": "PROD",
    "factory": "CheckFactory",
    "strategies": ["base", "check"],
    "tenancy": {
        "dsn": "postgresql://procesark:procesark@localhost/procesark"
    },
    "zones": {
        "default": {
            "dsn": "postgresql://procesark:procesark@localhost/procesark"
        }
    }
}}
