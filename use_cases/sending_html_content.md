# Sending HTML-only Content


Currently, we require both HTML and Plain Text content for improved deliverability. In some cases, only HTML may be available. The below example shows how to obtain the Plain Text equivalent of the HTML content.

## Using `beautifulsoup4`

```python
import os
from sowemail import SoWeMailAPIClient
from sowemail.helpers.mail import From, To, Subject, HtmlContent, Content, Mail
import urllib.request as urllib
from bs4 import BeautifulSoup

html_text = """
<html>
    <body>
        <p>
            Some
            <b>
                bad
                <i>
                    HTML
                </i>
            </b>
        </p>
    </body>
</html>
"""

sow_client = SoWeMailAPIClient(api_key=os.environ.get('SOWEMAIL_API_KEY'))
from_email = From("from_email@exmaple.com")
to_email = To("to_email@example.com")
subject = Subject("Test Subject")
html_content = HtmlContent(html_text)

soup = BeautifulSoup(html_text)
plain_text = soup.get_text()
plain_text_content = Content("text/plain", plain_text)

message = Mail(from_email, to_email, subject, plain_text_content, html_content)

try:
    response = sow_client.send(message=message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except urllib.HTTPError as e:
    print(e.read())
    exit()
```
