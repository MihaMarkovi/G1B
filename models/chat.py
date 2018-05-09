from google.appengine.ext import ndb

class Chat(ndb.Model):
    content = ndb.TextProperty()
    author_email = ndb.StringProperty()
    author_nickname = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    @classmethod
    def create(cls, content, user):
        chat = cls(content=content, author_email=user.email(), author_nickname=user.nickname())
        chat.put()
        return chat

    @classmethod
    def delete(cls, chat):
        chat.deleted=True
        chat.put()

        return chat
