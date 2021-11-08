from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def read_df():
    df = pd.read_csv("final.csv")
    return df

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/filter/", methods=['GET', 'POST'])
def filter():
    if request.method == "GET":
        df = read_df() 
        loc = df['Location'].unique()
        dur = df['Duration'].unique()
        pro = df['profile'].unique()
        d={}
        for i in df['Skills and Perks'].values:
            for j in eval(i):
                j = j.strip().lower()
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        skills = d.keys()
        return render_template("form.html", loc=loc, dur=dur, pro=pro, skills=skills)
    else:
        loc = request.form.get("location")
        pro = request.form.get("profile")
        dur = request.form.get("duration")
        skill = request.form.get("skill")
        df = read_df()
        temp = df.copy()
        if pro != "None":
            temp = df[df['profile'] == pro]
        if loc != "None":
            temp = temp[temp['Location'] == loc]
        if dur != "None":
            temp = temp[temp['Duration'] == dur]
        if skill != "None":
            temp = temp[temp['Skills and Perks'].apply(lambda x:True if skill.lower() 
                                    in list(map(lambda x: x.lower(), eval(x))) else False)]
        return render_template("show.html", tables=[temp.to_html(classes='myclass')])
        #return f"{loc}\t{pro}\t{dur}\t{skill}"

app.run(debug=True, port=80)