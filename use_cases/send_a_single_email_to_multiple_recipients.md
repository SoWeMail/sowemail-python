```python
import os
from sowemail import SoWeMailAPIClient
from sowemail.helpers.mail import Mail

to_emails = [
    ('test0@example.com', 'Example Name 0'),
    ('test1@example.com', 'Example Name 1')
]
message = Mail(
    from_email=('from@example.com', 'Example From Name'),
    to_emails=to_emails,
    subject='Hello from SoWeMail',
    html_content='<strong>Simple email sending example using python\'s sowerest library</strong>')
try:
    sow_client = SoWeMailAPIClient(os.environ.get('SOWEMAIL_API_KEY'))
    response = sow_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```
