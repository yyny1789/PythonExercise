from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://python.org/')
result = r.html.links
print(result)