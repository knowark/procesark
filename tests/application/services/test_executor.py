from procesark.application.models import Process
from procesark.application.services import Executor, MemoryExecutor


def test_executor_methods() -> None:
    methods = Executor.__abstractmethods__  # type: ignore
    assert 'execute' in methods
    assert 'invoke' in methods


def test_memory_executor_implementation() -> None:
    assert issubclass(MemoryExecutor, Executor)


async def test_memory_executor_execute() -> None:
    executor = MemoryExecutor()
    processes = [Process(id="001"), Process(id="002")]
    await executor.execute(processes)
    assert executor.executed == processes


async def test_memory_executor_invoke() -> None:
    executor = MemoryExecutor()
    processes = [Process(id="001"), Process(id="002")]
    result = await executor.invoke(processes)
    assert result == [executor.result, executor.result]
    assert executor.invoked == processes
