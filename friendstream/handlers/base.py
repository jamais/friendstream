import tornado
from lib import momoko

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        """
        in order to prevent blocking database calls, getting db instance here with momoko.AsyncClient
        """
        if not hasattr(self.application, 'db'):
            self.application.db = momoko.AsyncClient({
                'host'    : self.settings.get("postgresql_info").get("host"),
                'database': self.settings.get("postgresql_info").get("name"),
                'user'    : self.settings.get("postgresql_info").get("user"),
                'password': self.settings.get("postgresql_info").get("pass"),
                'min_conn': 1,
                'max_conn': 20,
                'cleanup_timeout': 10,
            })
        return self.application.db

    def get_current_user(self):
        raise NotImplementedError