from procesark.application.models import Run


def test_run_instantiation():
    run = Run(id='001', process_id='001', job_id='001')

    assert run.id == '001'
    assert run.process_id == '001'
    assert run.job_id == '001'
    assert run.state == ''
    assert run.start == 0
    assert run.end == 0
