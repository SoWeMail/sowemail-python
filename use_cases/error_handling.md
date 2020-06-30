# Error Handling

Please see [here](https://github.com/sowemail/sowerest-python/blob/master/sowerest/exceptions.py) for a list of supported exceptions.

There are also email specific exceptions located [here](https://github.com/sowemail/sowemail-python/blob/master/sowemail/helpers/mail/exceptions.py)

```python
  import os
  from sowemail import SoWeMailAPIClient
  from sowemail.helpers.mail import (From, To, Subject, PlainTextContent, HtmlContent, Mail)
  from sowerest import exceptions

  sow_client = SoWeMailAPIClient(os.environ.get('SOWEMAIL_API_KEY'))
  from_email = From("help@sowemail.com")
  to_email = To("dimitri@sowemail.com")
  subject = Subject("Hello from SoWeMail")
  plain_text_content = PlainTextContent("Simple email sending example using python's sowerest library")
  html_content = HtmlContent("<strong>Simple email sending example using python's sowerest library</strong>")
  message = Mail(from_email, to_email, subject, plain_text_content, html_content)
  try:
      response = sow_client.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except exceptions.BadRequestsError as e:
      print(e.body)
      exit()
```
