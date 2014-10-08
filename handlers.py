import tornado.web

class GameHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/game.html")

class ErrorPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Error")
