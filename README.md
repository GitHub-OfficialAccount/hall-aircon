# hall-aircon

Automate ntu hall aircon with pure python.

The only thing you need to get is your personal authorization token. If you have your own ways to get it, ignore everything below.

Prereq:
1. rooted android machine (VM, physical device, or Windows Subsystem for Android). Magisk is recommended for rooting. For me, I simply downloaded a rooted version of WSA.
2. an android program to intercept network traffic (e.g. Reqable)

Steps to get the token:
1. Follow the steps in Reqable to download the root system certificate.
2. Add Hall Aircon app to Reqable. Open Hall Aircon app.
3. Control Hall Aircon app. You will see different requests in Reqable, depending on what you do.
4. Find your personal bearer token in the request. Do not leak it.

How to control:
1. Simple way: just check auto.py and modify what you want to do.
2. More: check the requests and explore yourself.
