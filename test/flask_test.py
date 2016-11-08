from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def sel_team():
    return render_template('setup.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():

    if request.method == 'POST':

      team = request.form['Team']
      delay = request.form['Delay']
   
      result = { 'team' : team, 'delay' : delay }
      print("Result : {}".format(result))
      print (time)      
      return render_template("result.html",result = result)
            

if __name__ == '__main__':

	global time
	time = 20
	app.run(host= '0.0.0.0', debug=True)
