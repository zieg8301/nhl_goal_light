from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/options')
def sel_team():
    return """<html>
                <body>
                    Choose team :
                    <select>
                        <option value="canadiens">Canadiens</option>
                        <option value="Bruins">Bruins</option>
                    </select>
                </body>
            </html>"""

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
