import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():

    # Connect to the database and return the connection object
    db = sqlite3.connect(".database/mr.db")
    db.row_factory = sqlite3.Row

    return db

def GetAllReviews():

    # Connect, query all reviews and then return the data
    db = GetDB()
   
    reviews = db.execute("""SELECT Reviews.date, Reviews.title, Reviews.rating, Reviews.review, Users.username
                            FROM Reviews JOIN Users ON Reviews.user_id = Users.id
                            ORDER BY date DESC""").fetchall()

    db.close()
    return reviews

def CheckLogin(username, password):

    db = GetDB()

    # Ask the database for a single user matching the provided name
    user = db.execute("SELECT * FROM Users WHERE username=?", (username,)).fetchone()

    # Do they exist?
    if user is not None:
        # OK they exist, is their password correct
        if check_password_hash(user['password'], password):
            # They got it right, return their details
            return user
       
    # If we get here, the username or password failed.
    return None

def RegisterUser(username, password):

    # Check if they gave us a username and password
    if username is None or password is None:
        return False

    # Attempt to add them to the database
    db = GetDB()
    hash = generate_password_hash(password)
    db.execute("INSERT INTO Users(username, password) VALUES(?, ?)", (username, hash,))
    db.commit()

    return True

def AddReview(user_id, date, title, rating, review):
   
    # Check if any boxes were empty
    if date is None or title is None or review is None:
        return False
   
    # Get the DB and add the reviews
    db = GetDB()
    db.execute("INSERT INTO Reviews(user_id, date, title, rating, review) VALUES (?, ?, ?, ?, ?)",
               (user_id, date, title, rating, review))
    db.commit()

    return True

def deleteReview(id):

    conn = GetDB()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
