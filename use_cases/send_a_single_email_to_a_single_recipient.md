```python
import os
from sowemail import SoWeMailAPIClient
from sowemail.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Hello from SoWeMail',
    html_content='<strong>Simple email sending example using python\'s sowerest library</strong>')
try:
    sow_client = SoWeMailAPIClient(os.environ.get('SOWEMAIL_API_KEY'))
    response = sow_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
```
