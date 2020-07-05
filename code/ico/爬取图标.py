import requests as r
code = r.get('https://www.hetao101.com/favicon.ico')
with open('app.ico','wb') as f:
    f.write(code.content)