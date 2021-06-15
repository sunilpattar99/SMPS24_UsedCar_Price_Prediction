from flask import Flask, render_template, request, make_response
from predictionModel import predict_price
import uuid
import pdfkit

app = Flask(__name__)

@app.route('/')
def start_report():
    return render_template("home.html")

@app.route("/get_report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        req = request.form
        companyName = req["companyName"]
        modelName = req["modelName"]
        yom = req["yearOfManufacture"]
        city = req["city"]
        fuelType = req["fuelType"]
        ownerType = req["ownerType"]
        kilometer = req["kilometer"]
        engine = req["engine"]
        power = req["power"]
        mileage = req["mileage"]
        seats = req["seats"]
        transmission = req["transmission"]
    k = kilometer.split()[0]
    e = engine.split()[0]
    m = mileage.split()[0]
    p = power.split()[0]
    unique = uuid.uuid1()
    price = predict_price(int(yom), float(k), float(m), float(e),float(p), float(seats), city, fuelType, transmission, ownerType)
    return render_template("report.html",
     companyName=companyName,
     modelName=modelName,
     yom=yom,
     city=city,
     fuelType=fuelType,
     ownerType=ownerType,
     kilometer=kilometer,
     engine=engine,
     power=power,
     mileage=mileage,
     seats=seats,
     transmission=transmission,
     price=price,
     unique=unique
     )



app.run(debug=True, host='localhost')
