from typing import List
from asyncio import sleep
from datetime import datetime, timezone
from procesark.application.models import Trigger
from procesark.application.services import Scheduler, StandardScheduler


def test_scheduler_methods() -> None:
    methods = Scheduler.__abstractmethods__  # type: ignore
    assert 'schedule' in methods
    assert 'subscribe' in methods
    assert 'start' in methods
    assert 'stop' in methods


def test_standard_scheduler_implementation() -> None:
    assert issubclass(StandardScheduler, Scheduler)


def test_standard_scheduler_default_attributes() -> None:
    scheduler = StandardScheduler()
    assert scheduler.triggers == set()
    assert scheduler.subscribers == set()
    assert scheduler.active is False
    assert scheduler.tick == 1


async def test_standard_scheduler_schedule() -> None:
    triggers = [Trigger(id='001', process_id='001'),
                Trigger(id='002', process_id='002')]

    scheduler = StandardScheduler()
    await scheduler.schedule(triggers)

    assert scheduler.triggers == set(triggers)


async def test_standard_scheduler_subscribe() -> None:
    async def mock_callable(triggers: List[Trigger]) -> None:
        pass

    scheduler = StandardScheduler()
    await scheduler.subscribe(mock_callable)

    assert mock_callable in scheduler.subscribers


async def test_standard_scheduler_start() -> None:
    scheduler = StandardScheduler()
    trigger_1 = Trigger(id='001', process_id='001', pattern='*!1 * * * *')
    trigger_2 = Trigger(id='002', process_id='002', pattern='*!2 * * * *')

    calls = []

    async def mock_callable(triggers: List[Trigger]) -> None:
        nonlocal calls
        calls.extend(triggers)

    await scheduler.schedule([trigger_1, trigger_2])
    await scheduler.subscribe(mock_callable)

    await scheduler.start()
    await scheduler.start()  # check idempotency

    await sleep(2)

    assert len(calls) == 3
    assert calls.count(trigger_1) == 2
    assert calls.count(trigger_2) == 1


async def test_standard_scheduler_stop() -> None:
    scheduler = StandardScheduler()
    trigger_1 = Trigger(id='001', process_id='001', pattern='*!1 * * * *')
    trigger_2 = Trigger(id='002', process_id='002', pattern='*!2 * * * *')

    calls = []

    async def mock_callable(triggers: List[Trigger]) -> None:
        nonlocal calls
        calls.extend(triggers)

    await scheduler.schedule([trigger_1, trigger_2])
    await scheduler.subscribe(mock_callable)
    await scheduler.start()

    await sleep(1)

    await scheduler.stop()
    await scheduler.stop()  # check idempotency

    await sleep(1)

    assert len(calls) <= 2
    assert calls.count(trigger_1) == 1
    assert calls.count(trigger_2) <= 1


async def test_standard_scheduler_notify() -> None:
    scheduler = StandardScheduler()
    trigger_1 = Trigger(
        id='001', process_id='001', pattern='* * * * *')

    calls = []

    async def mock_callable(triggers: List[Trigger]) -> None:
        nonlocal calls
        calls.extend(triggers)

    now = datetime.now(timezone.utc)

    await scheduler._notify(now)

    assert len(calls) == 0

    await scheduler.subscribe(mock_callable)

    await scheduler._notify(now)

    assert len(calls) == 0

    await scheduler.schedule([trigger_1])

    await scheduler._notify(now)

    assert len(calls) == 1
