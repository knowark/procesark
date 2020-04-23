from pytest import fixture
from procesark.application.models import Trigger
from procesark.application.coordinators import LaunchCoordinator
from procesark.application.utilities import QueryParser
from procesark.application.repositories import MemoryTriggerRepository


@fixture
def trigger_repository(tenant_provider, auth_provider):
    trigger_repository = MemoryTriggerRepository(
        QueryParser(), tenant_provider, auth_provider)
    trigger_repository.load({'default': {
        '001': Trigger(id='001', process_id='002'),
        '002': Trigger(id='002', process_id='001')
    }})
    return trigger_repository


@fixture
def launch_coordinator(process_repository, job_repository,
                       allocation_repository, trigger_repository,
                       scheduler, executor):
    return LaunchCoordinator(
        process_repository, job_repository, allocation_repository,
        trigger_repository, scheduler, executor)


def test_launch_coordinator_methods(
        launch_coordinator: LaunchCoordinator):
    assert hasattr(launch_coordinator, 'prepare')
    assert hasattr(launch_coordinator, 'launch')


async def test_launch_coordinator_prepare(launch_coordinator):
    assert len(launch_coordinator.scheduler.triggers) == 0

    await launch_coordinator.prepare()

    assert len(launch_coordinator.scheduler.triggers) == 2
    assert launch_coordinator.scheduler.active is True


async def test_launch_coordinator_prepare(launch_coordinator):
    assert len(launch_coordinator.scheduler.triggers) == 0

    await launch_coordinator.prepare()

    assert len(launch_coordinator.scheduler.triggers) == 2


async def test_launch_coordinator_launch(launch_coordinator):
    triggers = [Trigger(id='001', process_id='002')]

    await launch_coordinator.launch(triggers)

    processes = launch_coordinator.executor.executed
    assert len(processes) == 1
    assert processes[0].id == '002'
