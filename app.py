from flask import Flask,request,render_template
import pickle
app=Flask(__name__)
model1 = pickle.load(open('model1.pkl', 'rb'))
model2 = pickle.load(open('model2.pkl', 'rb'))
model3 = pickle.load(open('model3.pkl', 'rb'))
@app.route('/')
def model():
    #features =[[float(x) for x in request.form.values()]]
    features=[[3,0.536,1,1,0]] 
    prediction=model1.predict(features)
    print("Returning value",prediction)
    #return {"Answer: ":prediction}
    return 'You can take : {} '.format(prediction)




if __name__ == '__main__':
    app.run(debug=True)