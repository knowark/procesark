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


async def test_standard_scheduler_schedule() -> None:
    triggers = [Trigger(id='001', process_id='001'),
                Trigger(id='002', process_id='002')]

    scheduler = StandardScheduler()
    await scheduler.schedule(triggers)

    assert scheduler.triggers == set(triggers)


async def test_standard_scheduler_subscribe() -> None:
    async def mock_callable(trigger: Trigger) -> None:
        pass

    scheduler = StandardScheduler()
    await scheduler.subscribe(mock_callable)

    assert mock_callable in scheduler.subscribers
