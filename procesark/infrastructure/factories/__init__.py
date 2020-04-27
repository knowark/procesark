from injectark import FactoryBuilder
from .strategies import strategy_builder
from .base_factory import BaseFactory
from .check_factory import CheckFactory


factory_builder = FactoryBuilder([BaseFactory, CheckFactory])
