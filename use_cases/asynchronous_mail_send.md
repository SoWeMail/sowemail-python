# Asynchronous Mail Send

## Using `asyncio` (3.5+)

The built-in `asyncio` library can be used to send email in a non-blocking manner. `asyncio` helps us execute mail sending in a separate context, allowing us to continue the execution of business logic without waiting for all our emails to send first.

```python
from sowemail import SoWeMailAPIClient
from sowemail.helpers.mail import Content, Mail, From, To, Mail
import os
import asyncio


sow_client = SoWeMailAPIClient(
    api_key=os.environ.get('SOWEMAIL_API_KEY'))

from_email = From("test@example.com")
to_email = To("test1@example.com")

plain_text_content = Content("text/plain", "This is asynchronous sending test.")
html_content = Content("text/html", "<strong>This is asynchronous sending test.</strong>")

# instantiate `sowemail.helpers.mail.Mail` objects
em1 = Mail(from_email, to_email, "Message #1", plain_text_content)
em2 = Mail(from_email, to_email, "Message #2", html_content)
em3 = Mail(from_email, to_email, "Message #3", plain_text_content)
em4 = Mail(from_email, to_email, "Message #4", html_content)
em5 = Mail(from_email, to_email, "Message #5", plain_text_content)
em6 = Mail(from_email, to_email, "Message #6", html_content)
em7 = Mail(from_email, to_email, "Message #7", plain_text_content)
em8 = Mail(from_email, to_email, "Message #8", html_content)
em9 = Mail(from_email, to_email, "Message #9", plain_text_content)
em10 = Mail(from_email, to_email, "Message #10", html_content)


ems = [em1, em2, em3, em4, em5, em6, em7, em8, em9, em10]


async def send_email(n, email):
    '''
    send_mail wraps SoWeMail's API client, and makes a POST request to
    the /v1/mail/send endpoint with `email`.
    Args:
        email<sowemail.helpers.mail.Mail>: single mail object.
    '''
    try:
        response = sow_client.send(request_body=email)
        if response.status_code < 300:
            print("Email #{} processed".format(n), response.body, response.status_code)
    except urllib.error.HTTPError as e:
        e.read()


@asyncio.coroutine
def send_many(emails, cb):
    '''
    send_many creates a number of non-blocking tasks (to send email)
    that will run on the existing event loop. Due to non-blocking nature,
    you can include a callback that will run after all tasks have been queued.

    Args:
        emails<list>: contains any # of `sowemail.helpers.mail.Mail`.
        cb<function>: a function that will execute immediately.
    '''
    print("START - sending emails ...")
    for n, em in enumerate(emails):
        asyncio.async(send_email(n, em))
    print("END - returning control...")
    cb()


def sample_cb():
    print("Executing callback now...")
    for i in range(0, 100):
        print(i)
    return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = asyncio.async(send_many(ems, sample_cb))
    loop.run_until_complete(task)
```
