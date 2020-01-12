from flask import Flask,request,render_template
import requests


app=Flask(__name__)

#json data
url="https://api.openweathermap.org/data/2.5/weather"
data=requests.get(url,params={"q":"india","appid":"578ff3e9d00030c7d290f89c49a5f9da"}).json()



#index data
@app.route("/")
def index():
    cities=["bengaluru","delhi","chennai","jaipur"]
    return render_template("index.html",object=cities)


@app.route("/result",methods=["POST","GET"])
def result():
    if request.method=="POST":
        city=request.form.get("city")
        
    data=requests.get(url,params={"q":city,"appid":"578ff3e9d00030c7d290f89c49a5f9da"}).json()
    return render_template("result.html",name=data)



if __name__=="__main__":
    app.run(debug=True)
