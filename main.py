from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
#set FLASK_APP = main.py
#flask --app main --debug run


@app.route("/", methods = ["GET", "POST"])
def index():
    
    if request.method == "GET":   
        return render_template("index.html")
    else:
        
        return buscar(request.form)



def buscar(dni):
    all_clients =  []
    client = []
    if request.method == "POST":
        with open("clientes.csv", "r", encoding="utf-8")as f:
            csvReader = csv.reader(f, delimiter=",", quotechar='"')
            for i in csvReader:
               all_clients.append(i[0].split(","))
            for i in all_clients:
                if i[2] == request.form["DNI"]:
                    client = i
               
               

    return render_template("client_viev.html", datos = client)



"""
if i[2] == request.form:
datos_cliente = i
"""