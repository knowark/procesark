from injectark import StrategyBuilder
from .base import base
from .check import check


strategy_builder = StrategyBuilder({
    'base':  base,
    'check':  check
})
