from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql
import mysql.connector

app = Flask(__name__)

# def connectivity():
#     db = sql.connect("templates/food.db")
#     cursor = db.cursor()
#     return db, cursor 

def database_CONNECTIVITY():
    db = mysql.connector.connect(host="sql545.main-hosting.eu",
                                 port=3306,
                                 user='u681323537_grras_SQL',
                                 password='5;YbQ1!JtPpY',
                                 db="u681323537_learnsql")

    myc = db.cursor()
    print("print myc: ",myc)
    return(myc,db)

@app.route('/',  methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        ID = request.form.get("ID")
        Name=request.form.get("name")
        Weight=request.form.get("weight")
        Height =request.form.get("height")
        Sex =request.form.get("sex")
        Age = request.form.get("age")

        cursor,db = database_CONNECTIVITY()

        cursor.execute(f"INSERT INTO user_food values ({ID},'{Name}',{Weight},{Height},'{Sex}',{Age})") 
        db.commit()
        # return f"{ID}\t{Name}\t{Weight}\t{Height}\t{Sex}\t{Age}"
        msg="User Succefuuly Added"
        return render_template("index.html",msg=msg)
    else:
        return render_template("index.html")
        

@app.route('/calin')
def caloriesin():
    cursor,db = database_CONNECTIVITY()

    cursor.execute(f"SELECT DISTINCT `Food Group` FROM `Food_Nutrition`;  ") 
    FoodGroup = [item[0] for item in cursor.fetchall()]
    cursor.execute(f"SELECT DISTINCT `ID` FROM `user_food`;  ") 
    ID= [item[0] for item in cursor.fetchall()]
    # cursor.execute(f"SELECT DISTINCT `name` FROM `Food_Nutrition`; ") 
    # FoodName = [item[0] for item in cursor.fetchall()]
    return render_template('caloriesin.html',FoodGroup=FoodGroup,ID=ID)  

@app.route('/sucscalin', methods=['GET', 'POST'])
def sucscalin():
    if request.method == 'POST':
        Date = request.form.get("date")
        ID = request.form.get("ID")
        FoodGroup = request.form.get("FG")
        FoodName = request.form.get("fn")
        

        # cursor,db = database_CONNECTIVITY()

        # cursor.execute(f"INSERT INTO user_food_calories values ({ID},'{FoodGroup}','{FoodName}',{FoodCalories})") 
        # db.commit()
        # msg="User Succefuuly Added"
        # return render_template("caloriesin.html",msg=msg)
        return f"{Date}\t{ID}\t{FoodGroup}\t{FoodName}"
    else:
        return f"NOTWORKING"


@app.route('/calout')
def caloriesout():
    cursor,db = database_CONNECTIVITY()

    cursor.execute(f"SELECT DISTINCT `Food Group` FROM `Food_Nutrition`;  ") 
    FoodGroup = [item[0] for item in cursor.fetchall()]

    cursor.execute(f"SELECT DISTINCT `ID` FROM `user_food`;  ") 
    ID= cursor.fetchall()
    # cursor.execute(f"SELECT DISTINCT `name` FROM `Food_Nutrition`; ") 
    # FoodName = [item[0] for item in cursor.fetchall()]
    return render_template('caloriesout.html',FoodGroup=FoodGroup,ID=ID)


@app.route('/showuser',  methods=['GET'] )
def showuser():
    cursor,db = database_CONNECTIVITY()
    cursor.execute("SELECT * FROM user_food limit 3")
    data = cursor.fetchall()
    return render_template("index.html",data=data)

@app.route('/showalluser',  methods=['GET'] )
def showalluser():
    cursor,db = database_CONNECTIVITY()
    cursor.execute("SELECT * FROM user_food")
    data = cursor.fetchall()
    return render_template("index.html",data=data)


@app.route('/about')
def about():
    return render_template("about.html")

app.run(debug=True, port=80)