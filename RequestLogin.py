id = 'userName'
id = 'password'

import requests



payload = {"userName":"longhaogao@gmail.com", "password":"somePass"}
r = requests.post("https://www.att.com/my/#/login", data=payload)
print(r)

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post("https://www.att.com/my/#/login", data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print p.text

    # An authorised request.
    #r = s.get('A protected web page url')
    #print(r)

