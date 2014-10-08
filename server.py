import tornado.ioloop
import tornado.web
import tornado.options
from core.uri_mapping import URI_MAPPING

cribbage = tornado.web.Application(URI_MAPPING)

if __name__ == "__main__":
    tornado.options.options['log_file_prefix'].set('/opt/logs/cribbage.log')
    tornado.options.parse_command_line()
    cribbage.listen(8880)
    tornado.ioloop.IOLoop.instance().start()
