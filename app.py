from flask import Flask, render_template, request, redirect
import csv
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    f = open("soccer.csv", "r", encoding="utf-8")
    soccers = csv.reader(f)
    return render_template("index.html", soccers=soccers)
 


@app.route('/new')
def new():
    return render_template("new.html")
    
    
@app.route('/res', methods=['post'])
def res():
    name = request.form.get("name")
    team = request.form.get("team")
    now = datetime.datetime.now()

    f = open("soccer.csv", "a+", encoding="utf-8", newline="")
    csv_w = csv.writer(f)
    csv_w.writerow([name, team, now])
    f.close()
    
    # return redirect("/")
    return render_template("res.html", name=name, team=team, now=now)





if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)