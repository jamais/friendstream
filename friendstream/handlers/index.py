import tornado

from base import BaseHandler

class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        return self.render("index.html")