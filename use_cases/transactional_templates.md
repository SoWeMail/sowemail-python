# Transactional Templates

For this example, we assume you have created a transactional template in your SoWeMail account. Following is the template content we used for testing.

Email Subject:

```text
{{ subject }}
```

Template Body:

```html
<html>
<head>
    <title></title>
</head>
<body>
Hello {{ name }},
<br /><br/>
I'm glad you are trying out the template feature!
<br /><br/>
I hope you are having a great day in {{ city }} :)
<br /><br/>
</body>
</html>
```

```python
import os
from sowemail import SoWeMailAPIClient
from sowemail.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    html_content='<strong>Simple email sending example using python\'s sowerest library</strong>')
message.dynamic_template_data = {
    'subject': 'Testing Templates',
    'name': 'Some One',
    'city': 'Denver'
}
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

## Prevent Escaping Characters

Per Handlebars' documentation: If you don't want Handlebars to escape a value, use the "triple-stash", {{{

> If you include the characters ', " or & in a subject line replacement be sure to use three brackets.

Email Subject:

```text
{{{ subject }}}
```

Template Body:

```html
<html>
<head>
    <title></title>
</head>
<body>
Hello {{{ name }}},
<br /><br/>
I'm glad you are trying out the template feature!
<br /><br/>
<%body%>
<br /><br/>
I hope you are having a great day in {{{ city }}} :)
<br /><br/>
</body>
</html>
```

```python
import os
from sowemail import SoWeMailAPIClient
from sowemail.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Hello from SoWeMail',
    html_content='<strong>Simple email sending example using python\'s sowerest library</strong>')
message.dynamic_template_data = {
    'subject': 'Testing Templates & Stuff',
    'name': 'Some "Testing" One',
    'city': '<b>Denver<b>',
}
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
