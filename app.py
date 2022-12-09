import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd




app=Flask(__name__)
#Load the model
rfmodel=pickle.load(open('rfmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('new.html')




@app.route('/predict', methods=['POST'])
def predict():
    team_code=int('50')
    opp_code=int('0')
    result=''
    if request.method == 'POST':
        
        home_team = request.form['home_team']
        print(home_team)
        if home_team == 'ARSENAL':
            team_code = 0
        elif home_team == 'CHELSEA':
            team_code = 1
        elif home_team == 'MANCHESTER-UNITED':
            team_code = 4
        elif home_team == 'MANCHESTER-CITY':
            team_code = 18
        elif home_team == 'EVERTON':
            team_code = 22
        elif home_team == 'NEW-CASTLE-UNITED':
            team_code = 21
        elif home_team == 'Tottenham':
            team_code = 12
        elif home_team == 'LIVERPOOL':
            team_code = 9
        print(team_code)  
            
        away_team = request.form['away_team']
        if away_team == 'Arsnel':
            opp_code = 0
        elif away_team == 'CHELSEA':
            opp_code = 1
        elif away_team == 'MANCHESTER-UNITED':
            opp_code = 4
        elif away_team == 'MANCHESTER-CITY':
            opp_code = 18
        elif away_team == 'EVERTON':
            opp_code = 22
        elif away_team == 'NEW-CASTLE-UNITED':
            opp_code = 21
        elif away_team == 'Tottenham':
            opp_code = 12
        elif away_team == 'LIVERPOOL':
            opp_code = 9
         
        

        
         
        venue = int(request.form['venue'])
        hour = int(request.form['hour'])
        day = int(request.form['day'])
        
        
        data = [team_code,opp_code,venue,hour,day]
        
        test_data=np.array(list(data)).reshape(1,-1) 
            
        my_prediction = rfmodel.predict(test_data)
        print(test_data)
        print(my_prediction[0])
        if my_prediction[0] == 1:
            result = home_team
        elif my_prediction[0] == 0:
            result= away_team  
        print(result)     
        return render_template('results.html', final=result)

if __name__=="__main__":
    app.run(debug=True)
    