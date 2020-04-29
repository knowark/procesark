from pytest import fixture
from procesark.application.coordinators import StageCoordinator


@fixture
def stage_coordinator(process_repository, job_repository,
                      allocation_repository, trigger_repository):
    return StageCoordinator(
        process_repository, job_repository, allocation_repository,
        trigger_repository)


def test_stage_coordinator_instantiation(
        stage_coordinator: StageCoordinator) -> None:
    assert hasattr(stage_coordinator, 'allocate')


async def test_stage_coordinator_allocate(stage_coordinator):
    allocation_dicts = [
        {'id': '001', 'process_id': '001', 'job_id': '001', 'sequence': 1},
        {'id': '002', 'process_id': '001', 'job_id': '002', 'sequence': 2},
        {'id': '003', 'process_id': '001', 'job_id': '003', 'sequence': 3},
        {'id': '004', 'process_id': '001', 'job_id': '005', 'sequence': 4}
    ]

    await stage_coordinator.allocate(allocation_dicts)

    allocations = stage_coordinator.allocation_repository.data['default']

    assert len(allocations) == 4
    for record in allocation_dicts:
        assert record['id'] in allocations


async def test_stage_coordinator_set_processes(stage_coordinator):
    process_dicts = [
        {'id': '003', 'name': 'Update System Dependencies'},
        {'id': '004', 'name': 'Deploy Website'},
    ]

    await stage_coordinator.set_processes(process_dicts)

    processes = stage_coordinator.process_repository.data['default']

    assert len(processes) == 4
    for record in process_dicts:
        assert record['id'] in processes


async def test_stage_coordinator_set_triggers(stage_coordinator):
    trigger_dicts = [
        {'id': '001', 'process_id': '001'},
        {'id': '002', 'process_id': '002'}
    ]

    await stage_coordinator.set_triggers(trigger_dicts)

    triggers = stage_coordinator.trigger_repository.data['default']

    assert len(trigger_dicts) == 2

    for record in trigger_dicts:
        assert record['id'] in triggers


async def test_stage_coordinator_delete_processes(stage_coordinator):
    await stage_coordinator.delete_processes(['001'])

    processes = stage_coordinator.process_repository.data['default']

    assert len(processes) == 1
    assert '002' in processes
