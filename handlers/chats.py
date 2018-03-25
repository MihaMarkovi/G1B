from handlers.base import BaseHandler
from google.appengine.api import users
from google.appengine.api import memcache
import uuid

from models.chat import Chat
from utils.decorators import validate_csrf


class Chats(BaseHandler):
    def get(self):
        csrf_token = str(uuid.uuid4())
        memcache.add(key=csrf_token, value=True, time=600)
        seznam = Chat.query( Chat.deleted == False).order(+Chat.updated).fetch()
        params = {"csrf_token": csrf_token, "seznam": seznam}

        return self.render_template("forum.html", params=params)

    @validate_csrf
    def post(self):
        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        text = self.request.get("text")
        Chat.create(content=text, user=user)

        # new_topic = Chat(title=title, content=text, author_email=user.email())
        # new_topic.put()
        #  put() saves the object in Datastore

        return self.redirect_to("chat-page")
