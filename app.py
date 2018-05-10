from flask import Flask, request, url_for, redirect, render_template, jsonify
import json

##Always going to be doing this for everything

'''Key Learning Goals
1. Defining routes and navigation between routes
2. Jinjas2 templating
3. Processing data from forms
4. Simple data storage using json
5. Build a fully functional app

Overview:
- Backend for login
- Backend for signup
- Backend for home page
- Backend for task entry page
- Rendering for home page
- Rendering for index page
- 22 items to complete
'''

app=Flask(__name__)

'''Allows users to go to the index page''' ##Must have it for each page
@app.route("/")
def index():
    #TODO:(4) Show different template renderings using name
    name="Sean"
    return render_template("index.html",name=name)

'''Allows users to login'''
@app.route("/login")
def login():
    return render_template("login.html")

'''Allows users to sign up'''
@app.route("/signup")
def signup():
    return render_template("signup.html")

'''Allows entries into the Todo List'''
@app.route("/entry")
def entry():
    return render_template("entry.html")




#TODO:(12) Add permissions for post requests
@app.route("/home",methods=["GET","POST"])
def home():
    #Data that will be injected into the template
    tasks = ["Cleaning the dishes", "Walking the dog", "Cooking dinner", "Playing basketball", "Practicing piano"]
    name={}

    # TODO:(22) Update the tasks with the ones from the "tasks.json" file

    #TODO:(13) Check post request

    if request.method == "POST":
        data = request.form
    #TODO:(14) Get the entered username
        username = data["username"]
        password = data["password"]

        with open("user.json", "w") as f:
            dbdata = json.load(f)
            db_username = dbdata["username"]
            db_password = dbdata["password"]

            if username == db_username and password == db_password:
                print("yay")

            return render_template(home.html, tasks = tasks, name = username)

    #TODO:(15) Check if the username and password match
    #TODO:(16) If there is a match, re-render the "home" page with the tasks and the username

    return render_template("home.html", tasks = tasks, name = name)

#TODO:(17) Check post request
#TODO:(18) Create an empty list for tasks
#TODO:(19) Get all of the tasks from the form and store in a var
#TODO:(20) Add all tasks to the task list
#TODO:(21) Write all of the tasks to the "tasks.json" file
@app.route("/confirm-entry",methods=["POST","GET"])
def confirm_entry():
    return render_template("confirm-entry.html")

#TODO:(1) Make a new route whose name is "confirm-signup"
#TODO:(3) Make the new route render the "confirm-signup" page
#TODO:(6) Allow post and get for the confirmation page

@app.route("/confirm-signup",methods=["POST","GET"])
def confirm_signup():
    if request.method == "POST":
        data = request.form
        print(data)

        user={}

        user["username"] = data["username"]
        user["password"] = data["password"]
        user["email"] = data["email"]

        print(user)

        with open("user.json", "w") as f:
            json.dump(user, f)

        return redirect(url_for("login"))
    return render_template("confirm-signup.html")


    '''Inside method'''
    #TODO:(7) Check post request form data

    #TODO:(8) Create variables from the posted data
    #TODO:(9) Store data in the "user" dictionary
    #TODO:(10) Store data in json file
    #TODO:(11) Server side redirect to "login" page

if __name__=="__main__":
    app.run(debug=True) #Never run as debug=True in a production environment

    # will help us see whats up with the code


