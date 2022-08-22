from prefect import flow, task

# this tasks runs 3 times before the flow fails
@task(retries=1, retry_delay_seconds=120)
def failure():
    print('running')
    raise ValueError("bad code")

@flow
def test_retries():
    return failure()
