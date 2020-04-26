from collections import defaultdict
from abc import ABC, abstractmethod


class Config(defaultdict, ABC):
    @abstractmethod
    def __init__(self):
        self["mode"] = "BASE"
        self["port"] = 6291
        self['strategies'] = ['base']
        self['strategy'] = {}
        self["tenancy"] = {
            "dsn": ""
        }
        self["zones"] = {
            "default": {
                "dsn": ""
            }
        }


class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self["mode"] = "DEV"
        self['factory'] = 'CheckFactory'
        self['strategies'].extend(['check'])


class ProductionConfig(Config):
    def __init__(self):
        super().__init__()
        self["mode"] = "PROD"
        self["factory"] = "SqlFactory"
        self['strategies'].extend(['sql'])
        self["tenancy"] = {
            "dsn": (
                "postgresql://questionark:questionark"
                "@localhost/questionark")
        }
        self["zones"] = {
            "default": {
                "dsn": ("postgresql://questionark:questionark"
                        "@localhost/questionark")
            }
        }
