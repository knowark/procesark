from procesark.application.models import Allocation


def test_allocation_instantiation():
    allocation = Allocation(id='001', process_id='001', job_id='001')

    assert allocation.id == '001'
    assert allocation.process_id == '001'
    assert allocation.job_id == '001'
