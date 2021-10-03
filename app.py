
from flask import Flask,render_template,request,session

from sklearn.metrics import accuracy_score
import joblib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/prediction1',methods=['POST','GET'])
def pred():
    a=[]
    if request.method=="POST":
        price = request.form['pp']
        popul = request.form['pl']
        income = request.form['mi']
        avgp = request.form['av']
        a.extend([price,popul,income,avgp])
        model=joblib.load('uber.pkl')
        y_pred=model.predict([a])
        return render_template('prediction.html',msg="done",op=y_pred)
    return render_template('prediction.html')


if __name__ == '__main__':
    app.secret_key="sahana"
    app.run(debug=True)



