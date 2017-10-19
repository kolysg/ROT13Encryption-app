#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import webapp2

# python 2 version for ROT13
def shiftVal(letter, n):
    shift_val = 13
    ascii_val = ord(letter) - n
    ascii_val += shift_val 
    return chr((ascii_val) % 26 + n)

def rot13(s):
    
    encrypted_message = ''

    for letter in s:
        if letter.isalpha() == True:

            if letter == letter.lower():
                encrypted_message += shiftVal(letter, 97)

            elif letter == letter.upper():
                encrypted_message += shiftVal(letter, 65)
        else:

            encrypted_message += letter

    return encrypted_message

# escape html
def escape_html(text):
    return cgi.escape(text,quote=True)

# text area form
form = '''
<div style = "display:table; margin:0 auto;font-size: 20px; font-weight:bold"> Enter some text to ROT13:</div>
<center>
    <form method = "post" action="/">
        <textarea rows="4" cols = "50" name = "q">%(text)s</textarea>
        <br>
        <input type = "submit">
    </form>
</center>
'''

class MainPage(webapp2.RequestHandler):
    
    def write_form(self, textInput=""):
        self.response.out.write(form % {"text" : escape_html(textInput)})

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get("q")
        # print("before text: ", user_text)
        if not user_text:
            self.write_form()
        else:
            user_text = self.request.get("q")
            user_text = rot13(user_text)
            user_text = escape_html(user_text)
            self.write_form(user_text)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


# apply redirection