from procesark.application.models import Process


def test_process_instantiation():
    process = Process(id='P001', name='Sales Data Sync Pipeline')

    assert process.id == 'P001'
    assert process.name == 'Sales Data Sync Pipeline'
    assert process.context == {}
