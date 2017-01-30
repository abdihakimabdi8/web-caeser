import webapp2
import caesar
import cgi
def build_page(textarea_content):

    message_form =  "<form method='post'><label>Message  </label><textarea name='message' cols='70' rows='20'>" + textarea_content + "</textarea></form>"
    return message_form

class MainHandler(webapp2.RequestHandler):

    def get(self):


        content =  "<form method='post'><label>Message   </label><textarea name='message'cols='60' rows='15'></textarea><br><label>Rotate By </label><input type='number' name='rotation'><input type='submit'></form>"
        header = "<h2 text-align='center'>Web Caesar</h2>"
        self.response.write( header + content)
    def post(self):
        message = self.request.get("message")
        rotation = self.request.get("rotation")

        encrypted_message = caesar.encrypt(message, rotation)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)
        rotaion_form = "<form><label>Rotate By </label><input type='number' name='rotation'><input type='submit'></form"
        header = "<h2>Web Caesar</h2>"
        self.response.write(header + content + rotaion_form)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
