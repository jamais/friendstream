import tornado

from base import BaseHandler

class IndexHandler(BaseHandler):

    @tornado.web.asynchronous
    def get(self):
        self.db.execute('SELECT pg_sleep(5); SELECT 636, 222, 123;',
            callback=self._on_response)

    def _on_response(self, cursor):
        print 'Request', cursor.fetchall()
        cursor.close()
        self.write('Hello Word!')
        self.finish()