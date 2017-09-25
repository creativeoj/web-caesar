from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True


form ="""
<!DOCTYPE html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px san-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
           
        </style>
        
    </head>
    <body> 
        <form action="/" method="post">
        <label for="Rotate-by:" >Rotate by: </label>
        <input type="text" name="rot" value="0" /> 
        <p><textarea cols=67 rows=5 name="text" value="text" >{0}</textarea></p>
        <input type="submit" value="submit query" /> 
    </body>
"""


@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():

    rot =  int(request.form["rot"])
    text = request.form["text"]
    encrypted_string = rotate_string(text, rot)
   

    if text == "" :
        error ='Enter empty string, Please input text in textarea'
        return form.format(error)
        
    
    else:
       return  '<h1>Encrypted string :' +form.format(encrypted_string)+'</h1>'
 

app.run()
