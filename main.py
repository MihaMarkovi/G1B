#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler, AboutHandler
from handlers.chats import Chats
from handlers.gallery import FotoHandler

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="cookie-alert"),
    webapp2.Route('/about', AboutHandler, name="about-page"),
    webapp2.Route('/fotogalerija', FotoHandler, name="foto-page"),
    webapp2.Route('/forum', Chats, name="chat-page"),
], debug=True)
