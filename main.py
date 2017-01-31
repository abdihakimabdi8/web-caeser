import webapp2
import caesar
import cgi
def build_page(textarea_content):

    message_form =  "<form method='post'><label>Message  </label><textarea name='message' cols='70' rows='20'>" + textarea_content + "</textarea><br><label>Rotate By </label><input type='number' name='rotation'><input type='submit'></form>"
    return message_form

class MainHandler(webapp2.RequestHandler):

    def get(self):
        content1 = build_page("")
        content = "<form method='post'><label>Rotate By </label><input type='number' name='rotation'><input type='submit'></form>"
        header = "<h2 text-align='center'>Web Caesar</h2>"
        self.response.write( header + content1)
    def post(self):
        message = self.request.get("message")
        rotation = self.request.get("rotation")

        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)
        rotaion_form = "<form method='post'><label>Rotate By </label><input type='number' name='rotation'><input type='submit'></form>"
        header = "<h2>Web Caesar</h2>"
        self.response.write(header + content)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
