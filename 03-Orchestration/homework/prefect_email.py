from prefect import flow
from prefect_email import EmailServerCredentials

@flow
def example_get_server_flow():
    email_server_credentials = EmailServerCredentials(
        username="felixpratama242@gmail.com",
        password="ahizbasvpbaattux",
    )
    server = email_server_credentials.get_server()
    return server

example_get_server_flow()
