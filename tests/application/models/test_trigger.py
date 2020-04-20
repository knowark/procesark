from procesark.application.models import Trigger


def test_trigger_instantiation():
    trigger = Trigger(id='001', process_id='001')

    assert trigger.id == '001'
    assert trigger.process_id == '001'
    assert trigger.type == 'direct'
