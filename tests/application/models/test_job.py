from procesark.application.models import Job


def test_job_instantiation():
    job = Job(id='J001', name='Download Sales Data')

    assert job.id == 'J001'
    assert job.name == 'Download Sales Data'
    assert job.context == {}
