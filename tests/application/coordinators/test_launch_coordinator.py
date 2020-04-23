# from pytest import fixture
# from procesark.application.coordinators import LaunchCoordinator


# @fixture
# def process_repository():
#     process_repository = MemoryProcessRepository()
#     process_repository.load({'default': {
#         Process(id='001', name='Sync Inventory Transactions'),
#         Process(id='002', name='Send Promotion Emails')
#     }})


# @fixture
# def launch_coordinator():
#     return LaunchCoordinator()


# def test_launch_coordinator_instantiation(
#         launch_coordinator: LaunchCoordinator) -> None:
#     assert hasattr(launch_coordinator, 'collect')
