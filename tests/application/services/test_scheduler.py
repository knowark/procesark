from procesark.application.models import Trigger
from procesark.application.services import Scheduler, StandardScheduler


def test_scheduler_methods() -> None:
    methods = Scheduler.__abstractmethods__  # type: ignore
    assert 'schedule' in methods
    assert 'subscribe' in methods


def test_standard_scheduler_implementation() -> None:
    assert issubclass(StandardScheduler, Scheduler)


def test_standard_scheduler_implementation() -> None:
    assert issubclass(StandardScheduler, Scheduler)


async def test_standard_scheduler_schedule() -> None:
    triggers = [Trigger(id='001', process_id='001'),
                Trigger(id='002', process_id='002')]
    scheduler = StandardScheduler()

    await scheduler.schedule(triggers)

    assert scheduler.triggers == triggers
