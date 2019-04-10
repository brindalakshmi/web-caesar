from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                background-color: #80A7AF;
                padding: 20px;
                margin: 5vh auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            h1 {{
                padding: 10vh 0 0 0;
            }}
            h1, p {{
                font-family: verdana;
                text-align: center;
                color: Red;
            }}
            input[type=submit] {{
                background-color: white;
                border: none;
                padding: 10px 22px;
            }}
            footer {{
                font-size: 14px;
                font-family: verdana;
                color: white;
                position: absolute;
                bottom: 0;
                right: 0;
            p.error {{
                color: red;
            }}
        </style>
    </head>
    <body>  
        <h1>Caesar Cipher</h1>
        <p><strong>Encryption: </strong>Enter a message and  number of letters to rotate the message by.</p>
            
  
      <form method="post">
          <label for="rot">Rotate by:</label>
          <input type="text" value="0" name= "rot">
          <p class="error"></p>
          <textarea type="text" name="text">{0}</textarea>
          <input type="submit"> 
      </form>
    </body>
</html>"""

@app.route("/")
def index():
    new_string = ""
    return form.format(new_string)


@app.route("/", methods=['POST'])
def encrypt():
    t = str(request.form["text"])
    r = int(request.form["rot"])
    rotated_string = rotate_string(t,r)
    result = "<h1>" + rotated_string + "</h1>"
    return form.format(rotated_string)

if __name__=="__main__":
    app.run()

app.run()


   
   


