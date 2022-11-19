import requests
from flask import Flask, render_template, request

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "L2b9n_p3zo6q3O4y9dDEELnvPDoruLIdD0lsYBSlicy2"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

city_dict={ "Ali" : 18 ,"Bar" : 2 ,"Ban" : 1 ,"Ch" :3,"Chid" :22,"Chit" :0,"Hyd" :6,"Kol":8,"Jai":15,"Moh":10,"Mum":11,"Man":7,"ND":13,
"Nag": 20,"Pal": 4,"Pali":12 ,"Pha":16 ,"Pu" :17 ,"Sa" :5 ,"Tiru":19 ,"Var":9 ,"Vel":21,"War":14 }

city_dict1={ "Ali" : "Aligarh" ,"Bar" : "Baroda" ,"Ban" : "Bangalore" ,"Ch" :"Chennai","Chid" :"Chidambaram","Chit":"Chitanukalan","Hyd":"Hydrabad","Kol":"Kolkata","Jai":"Jaipur","Moh":"Mohali","Mum":"Mumbai","Man":"Mangalore","ND":"New Delhi",
"Nag":"Nagpur","Pal": "Palani","Pali":"Pali" ,"Pha":"Phagwara" ,"Pu" :"Pune","Sa" :"Sawargaon" ,"Tiru":"Tiruchirappalli" ,"Var":"Varanasi","Vel":"Vellore","War":"Warangal" }
univ_dict={"AMU" : [23 ,80],"AU" : [37 , 60],"BHU" :[28 , 60],"BITS" : [24 ,75],"CHU":[20,55],"CU" :[5,40],"DTU" : [6,60],"GGSIU" :[10,50],
"ICTM" : [16,66],"IGNOU" :[14,55],"IISB" : [18,70],"IITB" : [15,50],"IITD" : [13,75],"IITM" :[12,55],"JH" : [17,50],"JMI" : [9,50],
"JNU" : [3 ,55],"JU" : [11,60],"LPU" :[4,55],"MGR" : [7,60],"MSUB" :[29,50],"MU" :[26 ,50 ],"NIMS" : [0,50],"NITK" : [2 ,75],"NITT" :[25,65],
"NITW" :[19 ,75],"PES" : [38,60],"PUB" : [22 , 45],"RU":[21,50],"SIST" :[31,45],"SPPU" : [32,55],"SRM" :[30,60],"TIU" : [8,60],"UD" : [34,45],
"UH" : [35,60],"VIT":[36,55],"VKMWPU" : [33,45],"VNIT" : [1 ,65],"YCMOU" :[27,40]}

headings=("University Name","State","District","College Link","Location Link","Entrance Percentage","Ranking","12th Percentage")
data=(("Aligarh Muslim University","Uttar Pradesh","Aligarh","https://www.amu.ac.in/","https://goo.gl/maps/bSXzBBmonzYchKdt9",80,11,55),
       ("Annamalai University","Tamil Nadu","Chidambaram","https://annamalaiuniversity.ac.in/index.php","https://goo.gl/maps/NEjmf5ZQxppHT5hc6",60,152,55),
       ("Banaras Hindu University","Uttar Pradesh","Varanasi","https://www.bhu.ac.in/","https://goo.gl/maps/Rakq5Nzp9nYeBRJs8",60,6,50),
       ("Birla Institute of Technology and Science","Tamil Nadu","Palani","https://www.bits-pilani.ac.in/","https://goo.gl/maps/SfpECfucmb3t8wAR7",75,15,75),
       ("Chandigarh University","Punjab","Mohali","https://www.cuchd.in/","https://g.page/ChandigarhUni?share",55,29,50),
       ("Christ University","Karnataka","Bangalore","https://christuniversity.in/","https://goo.gl/maps/kN6GTxWdqatbPvYv7",40,71,55),
       ("Delhi Technological University","New Delhi","New Delhi","http://www.dtu.ac.in/","https://goo.gl/maps/VHMGgd3YwdPJitHD8",60,36,60),
       ("Dr MGR Educational and Research Institute","Tamil Nadu","Chennai","https://www.drmgrdu.ac.in/","https://goo.gl/maps/tYMpvFVbBPnggCuy7",60,25,55),
       ("Dr Vishwanath Karad MIT World Peace University","Maharashtra","Pune","https://mitwpu.edu.in/","https://goo.gl/maps/wKQeTk9u8s8mHZz67",45,116,50),
       ("Guru Gobind Singh Indraprastha University","New Delhi","New Delhi","http://www.ipu.ac.in/","https://goo.gl/maps/YknYxUsX6m2MAXRXA",50,95,60),
       ("Indian Institute of Science, Bangalore","Karnataka","Bangalore","https://iisc.ac.in/","https://goo.gl/maps/GK9gUja8pnfSpFYL7",70,94,50),
       ("Indian Institute of Technology,Bombay","Maharashtra","Mumbai","https://www.iitb.ac.in/","https://goo.gl/maps/kbKqj6Z9bfGnERS39",50,80,60),
       ("Indian Institute of Technology,Madras","Tamil Nadu","Chennai","https://www.iitm.ac.in/","https://goo.gl/maps/73bHL5Q8RQS8yt5v9",55,153,55),
       ("Indian Institute of Technology,Delhi","New Delhi","New Delhi","https://home.iitd.ac.in/","https://goo.gl/maps/3gPFUWx7fp2A99fP6",75,160,60),
       ("Indira Gandhi National Open University","New Delhi","New Delhi","http://ignou.ac.in/","https://goo.gl/maps/SfsYq66L9xvvDFsbA",55,71,55),
       ("Institute of Chemical Technology, Mumbai","Maharashtra","Mumbai","https://www.ictmumbai.edu.in/","https://goo.gl/maps/Y6rD7yit6Kc7dH189",66,14,55),
       ("Jadavpur University","West Bengal","Kolkata","http://www.jaduniv.edu.in/","https://goo.gl/maps/dLSJoT2jB61XXBUZA",60,4,45),
       ("Jamia Hamdard","New Delhi","New Delhi","http://jamiahamdard.edu/","https://goo.gl/maps/z6S684pksuWb4vFs5",50,46,50),
       ("Jamia Millia Islamia","New Delhi","New Delhi","https://www.jmi.ac.in/","https://goo.gl/maps/NCaytJGjbrEMc3WU8",50,3,50),
       ("Jawaharlal Nehru University","Tamil Nadu","Pali","https://www.jnu.ac.in/","https://goo.gl/maps/s6VEFh8SNQ391jLs9",55,10,55),
       ("Lovely Professional University","Punjab","Phagwara","https://www.lpu.in/","https://g.page/LPUUniversity?share",55,47,60),
       ("Maharaja Sayajirao University of Baroda","Gujarat","Baroda","https://www.msubaroda.ac.in/","https://g.page/TheMSUB?share",50,90,40),
       ("Manipal University","Rajasthan","Jaipur","https://manipal.edu/mu.html","https://goo.gl/maps/JsuTibUDEocMwkxt9",50,103,50),
       ("National Institute of Technology Karnataka","Karnataka","Mangalore","https://www.nitk.ac.in/","https://goo.gl/maps/eRFnpagJi5i4z5yS9",75,64,60),
       ("National Institute of Technology Tiruchirappalli","Tamil Nadu","Tiruchirappalli","https://www.nitt.edu/","https://goo.gl/maps/jCdSeTTq88JgF1HJ8",65,47,75),
       ("National Institute of Technology, Warangal","Telangana","Warangal","https://www.nitw.ac.in/","https://goo.gl/maps/nE1XMKvb5eRTfo6f8",75,45,75),
       ("NIMS University","Rajasthan","Chitanukalan","https://www.nimsuniversity.org/","https://g.page/MyNIMS?share",50,101,45),
       ("PES University","Karnataka","Bangalore","https://pes.edu/","https://goo.gl/maps/6C2mn7kWp4JDaVz17",60,83,50),
       ("Presidency University, Bangalore","Karnataka","Bangalore","https://presidencyuniversity.in/","https://goo.gl/maps/Zvwj62U1qjGfV113A",45,62,50),
       ("REVA University","Karnataka","Bangalore","https://www.reva.edu.in/","https://goo.gl/maps/wW8DzUoECBTwBGJ79",50,151,45),
       ("Sathyabama Institute of Science and Technology","Tamil Nadu","Chennai","https://www.sathyabama.ac.in/","https://goo.gl/maps/QuVeBJuw7TNTMuQB7",45,43,45),
       ("Savitribai Phule Pune University","Maharashtra","Pune","http://www.unipune.ac.in/","https://goo.gl/maps/QoBB86cSLfgA5gei7",55,12,55),
       ("SRM Institute of Science and Technology","Tamil Nadu","Chennai","https://www.srmist.edu.in/","https://goo.gl/maps/z7BsZBg1coy96UdJ8",60,19,50),
       ("Techno India University","West Bengal","Kolkata","https://www.technoindiauniversity.ac.in/","https://g.page/tiuwestbengal?share",60,109,60),
       ("University of Delhi","New Delhi","New Delhi","http://www.du.ac.in/","https://goo.gl/maps/FRukDt7VQXdQfUJcA",45,13,50),
       ("University of Hyderabad","Telangana","Hyderabad","https://uohyd.ac.in/","https://g.page/hyderabad-central-university-hcu?share",60,10,60),
       ("Vellore Institute of Technology","Tamil Nadu","Vellore","https://vit.ac.in/","https://goo.gl/maps/hgQD3vdarwFDZP1eA",55,9,55),
       ("Visvesvaraya National Institute of Technology","Maharashtra","Nagpur","https://vnit.ac.in/","https://goo.gl/maps/VNnyPyWo7jZp5xCX7",65,54,75),
       ("Yashwantrao Chavan Maharashtra Open University","Maharashtra","Sawargaon","https://www.ycmou.ac.in/","https://goo.gl/maps/Dc2hzzR24nu5fjWg6",40,93,45)
)



app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
    return render_template("Home.html")

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/choose_dept', methods=['POST'])
def departments():
    dep = request.form["depts"]
    if(dep == "civil"):
        return render_template("civil.html")
    if(dep == "cse"):
        return render_template("cse.html")
    if(dep == "ece"):
        return render_template("ece.html")
    if(dep == "eee"):
        return render_template("eee.html")
    if(dep == "mech"):
        return render_template("mech.html")

@app.route('/civil',methods=['POST'])
def civil():
    d1_civil=[]
    d2_civil=[]
    u=0
    e=0
    percent= request.form.get('twelC',type=float)
    cities=request.form["citiesC"]
    univ = request.form["uniC"]
    for key in city_dict1:
        if key == cities:
            c=city_dict1[key]
    for key1 in univ_dict:
        if key1 == univ:
            x=univ_dict[key1]
            u = x[0]
            e = x[1]
    pred = [[u,int(percent),e,0]]  
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [['University Name','12th Percentage','Entrance Percentage','Department']], "values": pred}]}
    response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/ba6c6e10-7576-4d5d-9c73-ca1b9b4ebf21/predictions?version=2022-11-17', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})

    probability = response_scoring.json()['predictions'][0]['values'][0][0]
    i=0
    for ds in data:
            if(float(ds[7]) >= percent or c==ds[2]) and i<10:
                d1_civil.insert(i,ds)
                i+=1
    
    d2_civil = list(set(j for j in d1_civil))
    if(probability == 1):
        return render_template("output.html",prediction="Congrats You are Eligible", headings=headings,d2=d2_civil)
    else:
        return render_template("output.html",prediction="You are not eligible. Let's hope for the best",headings=headings,d2=d2_civil)
    

@app.route('/cse',methods=['POST'])
def cse():
    d1_cse=[]
    d2_cse=[]
    d=1
    percent1= request.form.get('twel',type=float)
    cities=request.form["cities"]
    univ = request.form["uni"]
    for key in city_dict1:
        if key == cities:
            c1=city_dict1[key]
    for key1 in univ_dict:
        if key1 == univ:
            x=univ_dict[key1]
            u1 = x[0]
            e1 = x[1]
    pred = [[u1,int(percent1),e1,d]]  
  # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [['University Name','12th Percentage','Entrance Percentage','Department']], "values": pred}]}
    response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/ba6c6e10-7576-4d5d-9c73-ca1b9b4ebf21/predictions?version=2022-11-17', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    

    probability = response_scoring.json()['predictions'][0]['values'][0][0]
    i1 = 0
    for ds in data:
        if(float(ds[7]) >= percent1 or c1==ds[2]) and i1 < 10:
            d1_cse.insert(i1,ds)
            i1 += 1
    
    d2_cse = list(set(j for j in d1_cse))
    if(probability == 1):
        return render_template("output.html",prediction="Congrats You are Eligible", headings=headings,d2=d2_cse)
    else:
        return render_template("output.html",prediction="You are not eligible. Let's hope for the best",headings=headings,d2=d2_cse)
    
@app.route('/ece',methods=['POST'])
def ece():
    d1_ece=[]
    d2_ece=[]
    d=3
    percent2= request.form.get('twelEC',type=float)
    cities=request.form["citiesEC"]
    univ = request.form["uniEC"]
    for key in city_dict1:
        if key == cities:
            c2=city_dict1[key]
    for key1 in univ_dict:
        if key1 == univ:
            x=univ_dict[key1]
            u2 = x[0]
            e2 = x[1]
    pred = [[u2,int(percent2),e2,d]]  
   # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [['University Name','12th Percentage','Entrance Percentage','Department']], "values": pred}]}
    response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/ba6c6e10-7576-4d5d-9c73-ca1b9b4ebf21/predictions?version=2022-11-17', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    

    probability = response_scoring.json()['predictions'][0]['values'][0][0]


    i2 = 0
    for ds in data:
            if(float(ds[7]) >= percent2 or c2==ds[2]) and i2 < 10:
                d1_ece.insert(i2,ds)
                i2 += 1
    
    d2_ece = list(set(j for j in d1_ece))
    if(probability == 1):
        return render_template("output.html",prediction="Congrats You are Eligible", headings=headings,d2=d2_ece)
    else:
        return render_template("output.html",prediction="You are not eligible. Let's hope for the best",headings=headings,d2=d2_ece)
    
@app.route('/eee',methods=['POST'])
def eee():
    d1_eee=[]
    d2_eee=[]
    d=2
    percent3= request.form.get('twelE',type=float)
    cities=request.form["citiesE"]
    univ = request.form["uniE"]
    for key in city_dict1:
        if key == cities:
            c3=city_dict1[key]
    for key1 in univ_dict:
        if key1 == univ:
            x=univ_dict[key1]
            u3 = x[0]
            e3 = x[1]
    pred = [[u3,int(percent3),e3,d]]  
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [['University Name','12th Percentage','Entrance Percentage','Department']], "values": pred}]}
    response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/ba6c6e10-7576-4d5d-9c73-ca1b9b4ebf21/predictions?version=2022-11-17', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})

    probability = response_scoring.json()['predictions'][0]['values'][0][0]
    i3=0
    for ds in data:
        if(float(ds[7]) >= percent3 or c3==ds[2]) and i3 < 10:
            d1_eee.insert(i3,ds)
            i3 += 1
    
    d2_eee = list(set(j for j in d1_eee))
    if(probability == 1):
        return render_template("output.html",prediction="Congrats You are Eligible", headings=headings,d2=d2_eee)
    else:
        return render_template("output.html",prediction="You are not eligible. Let's hope for the best",headings=headings,d2=d2_eee)
    
@app.route('/mech',methods=['POST'])
def mech():
    d1_mech=[]
    d2_mech=[]
    d=4
    percent4= request.form.get('twelM',type=float)
    cities=request.form["citiesM"]
    univ4 = request.form["uniM"]
    for key in city_dict1:
        if key == cities:
            c4=city_dict1[key]
    for key1 in univ_dict:
        if key1 == univ4:
            x=univ_dict[key1]
            u = x[0]
            e = x[1]
           
    pred = [[u,int(percent4),e,d]] 
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": [['University Name','12th Percentage','Entrance Percentage','Department']], "values": pred}]}
    response_scoring = requests.post('https://eu-de.ml.cloud.ibm.com/ml/v4/deployments/ba6c6e10-7576-4d5d-9c73-ca1b9b4ebf21/predictions?version=2022-11-17', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
    probability =  response_scoring.json()['prediction'][0]['values'][0][0]
    i4=0
    for ds in data:
            if(float(ds[7]) >= percent4 or c4==ds[2]) and i4 < 10:
                d1_mech.insert(i4,ds)
                i4 += 1
    
    d2_mech = list(set(j for j in d1_mech))
    if(probability == 1):
        return render_template("output.html",prediction="Congrats You are Eligible", headings=headings,d2=d2_mech)
    else:
        return render_template("output.html",prediction="You are not eligible. Let's hope for the best",headings=headings,d2=d2_mech)
    

if __name__ == '__main__':
    app.run(debug=True)