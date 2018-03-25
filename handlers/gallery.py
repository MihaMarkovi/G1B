from handlers.base import BaseHandler


class FotoHandler(BaseHandler):
    def get(self):
        return self.render_template("foto.html")