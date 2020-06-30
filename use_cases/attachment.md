# Attachment

```python
import base64
import os
from sowemail.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from sowemail import SoWeMailAPIClient

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Hello from SoWeMail',
    html_content='<strong>Simple email sending example using python\'s sowerest library</strong>')
file_path = 'example.pdf'
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/pdf')
attachment.file_name = FileName('test_filename.pdf')
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId('Example Content ID')
message.attachment = attachment
try:
    sow_client = SoWeMailAPIClient(os.environ.get('SOWEMAIL_API_KEY'))
    response = sow_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)

```
