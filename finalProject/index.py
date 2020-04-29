from flask import Flask,render_template,request
from backend import Main
import json


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/yeartemp', methods=['POST'])
def index():
    ob=Main();
    data=ob.globalTemp()
    labels = data.keys()
    values = data.values()
    #m=list(values)so not pass into  render_template
    #m=max(values)
    values = list(values)
    round_values = [round(num,4) for num in values]
    values = round_values
    return render_template('yearlyTemp.html',values=values, labels=labels)

@app.route('/', methods=['POST'])
def getValue():
    country = request.form['country']
    #state = request.form['state']
    city = request.form['city']
    ob=Main();
    data=ob.globalTempByCity(country,city)
    if(data is None):
        return render_template('404.html')
    else:
        #m=data.max() so not pass into  render_template because linenewcity
        data= dict(data)
        labels = data.keys()
        values = data.values()
        values = list(values)
        round_values = [round(num,4) for num in values]
        values = round_values
        return render_template('cityTemp.html', country=country,city=city,values=values,labels=labels)
 
@app.route('/line')
def line():
    return render_template('line.html')    

if __name__=='__main__':
    app.run(debug=True)
