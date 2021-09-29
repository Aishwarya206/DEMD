from flask import Flask,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def welcome():
   return render_template("index.html")

@app.route('/name/<your_name>',methods=['GET','POST'])
def names(your_name):
    return f"Welcome to Praxis {your_name}"

if __name__ == '__main__':
   app.run(debug=True,host="0.0.0.0",port=3400)

