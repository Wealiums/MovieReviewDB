from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "mr"

@app.route("/")
def Home():
    query = request.args.get('query')
    if query:
        reviewData = db.SearchReviews(query)
    else:
        reviewData = db.GetAllReviews()
    return render_template("index.html", reviews=reviewData)

@app.route("/login", methods=["GET", "POST"])
def Login():

    # They sent us data, get the username and password
    # then check if their details are correct.
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Did they provide good details
        user = db.CheckLogin(username, password)
        if user:
            # Yes! Save their username then
            session['username'] = user['username']
            session['id'] = user['id']

            # Send them back to the homepage
            return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def Register():

    # If they click the submit button, let's register
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # Try and add them to the DB
        if db.RegisterUser(username, password):
            # Success! Let's go to the homepage
            return redirect("/")
       
    return render_template("register.html")

@app.route("/add", methods=["GET","POST"])
def Add():

    # Check if they are logged in first
    if session.get('username') == None:
        return redirect("/")

    # Did they click submit?
    if request.method == "POST":
        user_id = session['id']
        date = request.form['date']
        title = request.form['title']
        rating = int(request.form['rating'])  # Convert rating to integer
        review = request.form['review']

        # Check if date is provided
        if not date:
            return "Error: Date is required.", 400

        # Send the data to add our new review to the db
        db.AddReview(user_id, date, title, rating, review)

    return render_template("add.html")

@app.route("/delete/<int:id>", methods=["POST"])
def Delete(id):
    if 'id' not in session:
        return redirect("/login")
    user_id = session['id']
    print(f"Attempting to delete review with ID: {id} by user ID: {user_id}")
    if db.DeleteReview(user_id, id):
        print("Review deleted successfully.")
        return redirect("/")
    else:
        print("Error: Review not found or you do not have permission to delete it.")
        return "Error: Review not found or you do not have permission to delete it.", 403

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def Edit(id):
    if 'id' not in session:
        return redirect("/login")
    
    user_id = session['id']
    
    if request.method == "POST":
        date = request.form['date']
        title = request.form['title']
        rating = int(request.form['rating'])  # Convert rating to integer
        review = request.form['review']
        
        if db.EditReview(user_id, id, date, title, rating, review):
            return redirect("/")
        else:
            return "Error: Could not update review.", 403
    
    review = db.GetDB().execute("SELECT * FROM Reviews WHERE id = ? AND user_id = ?", (id, user_id)).fetchone()
    if review is None:
        return "Error: Review not found or you do not have permission to edit it.", 403
    
    return render_template("edit.html", review=review)

@app.route("/delete_account", methods=["GET", "POST"])
def DeleteAccount():
    if 'id' not in session:
        return redirect("/login")
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        if db.DeleteAccount(username, password):
            session.clear()
            return redirect("/")
        else:
            return "Error: Incorrect username or password.", 403
    
    return render_template("deleteAccount.html")

app.run(debug=True, port=5000)
