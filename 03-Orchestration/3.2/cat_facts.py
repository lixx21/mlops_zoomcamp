import httpx
from prefect import flow, task

"""
    For TASK has an argumeents:
    1. retries that used to retry if the task were fail for some reason between each retry Prefect
    2. Prefect will also wait for period of time before trying to run the task again
    3. Prefect will print statements that are made within this task  will be shared within the logs whenever this script is run (which means we can see cat fact in the logs)

    For FLOW is simply will call a task
"""

@task(retries=4, retry_delay_seconds=0.1, log_prints=True)
def fetch_cat_fact():
    cat_fact = httpx.get("https://f3-vyx5c2hfpq-ue.a.run.app/")
    #An endpoint that is designed to fail sporadically
    if cat_fact.status_code >= 400:
        raise Exception()
    print(cat_fact.text)


@flow
def fetch():
    fetch_cat_fact()


if __name__ == "__main__":
    fetch()