
#importing necessary modules
from flask import Flask, render_template, request  
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb')) #Loading my model with pickle

@app.route('/')
def index():
        return render_template('about.html')
        return  app.send_static_file('wind-turbines.jpg') 
        

@app.route('/submit_form',methods=['POST','GET']) #Creating a submit form for user to enter the wind speed necessary values
def submit_form():
    return render_template('myform.html')# myform file is in 'templates' folder return using render_template method
    if request.method == 'POST':
        # Get the data from the POST request.
        data = request.form('text', type=int)
        return redirect(url_for('predict', pred=data)) #returning data entered through form as redirect url.
    else:
        print('Something went wrong here')


@app.route('/<pred>') #accessing to this adding the entered value into the route returns the plot with our model 
#prediction values in relation to the actual values
def predict(pred):
    
    return app.send_static_file('Prediction plot LR.png') 

 
if __name__=='__main__':
    app.run(debug=True, port=5000)

