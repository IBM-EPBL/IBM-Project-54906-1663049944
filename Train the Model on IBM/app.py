from flask import Flask ,render_template,request,redirect,url_for
import requests
from math import ceil
app = Flask(__name__)
import pickle
k=open("university.pkl","rb")
model = pickle.load(k)
@app.route("/index")
def index():
    return render_template('predict.html')

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        arr = []
        for i in request.form:
            val = request.form[i]
            if val == '':
                return redirect(url_for("predict"))
            arr.append(float(val))

        API_KEY = "wf8mge_OQdwVO8ao2kmWCtfxOfLWl8442SH44V85v2Ls"
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={
            "apikey": API_KEY, 
            "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'
            })
        mltoken = token_response.json()["access_token"]
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
        payload_scoring = {
            "input_data": [{"fields":[  'GRE Score',
                                        'TOEFL Score',
                                        'University Rating',
                                        'SOP',
                                        'LOR ',
                                        'CGPA',
                                        'Research'], 
                            "values": [arr]
                            }]
                        }

        response_scoring = requests.post(
            'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8308fd4c-24a5-46ab-96fa-263657ae4ad0/predictions?version=2022-10-18', 
            json=payload_scoring,
            headers=header
        ).json()
        
        result = response_scoring['predictions'][0]['values']
        
        if result[0][0] > 0.5:
            return redirect(url_for('chance', percent=ceil(result[0][0]*100)))
        else:
            return redirect(url_for('no_chance', percent=ceil(result[0][0]*100)))
@app.route("/chance/<percent>")
def chance(percent):
    return render_template("chance.html", p=percent)

@app.route("/nochance/<percent>")
def no_chance(percent):
    return render_template("NoChance.html", p=percent)
if __name__=='__main__':
    app.run()
