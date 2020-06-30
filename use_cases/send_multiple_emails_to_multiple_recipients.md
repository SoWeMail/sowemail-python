```python
import os
from sowemail import SoWeMailAPIClient
from sowemail.helpers.mail import Mail, To

to_emails = [
    To(email='test+to0@example.com',
       name='Example Name 0',
       dynamic_template_data={
           'name': 'Dynamic Name 0',
           'url': 'https://example.com/test0',
       },
       subject='Override Global Subject'),
    To(email='test+to1@example.com',
       name='Example Name 1',
       dynamic_template_data={
           'name': 'Dynamic Name 1',
           'url': 'https://example.com/test1',
       }),
]
message = Mail(
    from_email=('test+from@example.com', 'Example From Name'),
    to_emails=to_emails,
    subject='Global subject',
    is_multiple=True)
message.template_id = '13b8f94f-bcae-4ec6-f67a-70d6cb59f932'

try:
    sow_client = SoWeMailAPIClient(os.environ.get('SOWEMAIL_API_KEY'))
    response = sow_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
```
