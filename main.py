#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler, AboutHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert"),
    webapp2.Route('/about', AboutHandler, name="about-page"),
], debug=True)
