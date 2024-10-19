from flask import Flask,render_template,request
import pickle

with open('prediction.pkl','rb') as file:
    cl=pickle.load(file)

app=Flask(__name__)

@app.route('/',methods=["GET"])
def start():
    return 'veer'

@app.route('/form',methods=["GET","POST"])
def home():
    if request.method=="GET":
    # return 'hello world'
     return render_template ('index.html')
    else:
       hours=float(request.form['hours'])
    

    prediction=cl.predict([[hours]])

    return render_template('index.html',min=prediction[0][0])









if __name__=="__main__":
    app.run(debug=True)
