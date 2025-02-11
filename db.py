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
    reviews = db.execute("""SELECT Reviews.date, Reviews.title, Reviews.rating, Reviews.review, Users.username, Reviews.id
                            FROM Reviews JOIN Users ON Reviews.user_id = Users.id
                            ORDER BY Reviews.date DESC, Reviews.id DESC""").fetchall()
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
    if not date or not title or not review:
        return False

    # Validate rating
    rating = int(rating)
    if rating < 1 or rating > 5:
        return False

    # Get the DB and add the reviews
    db = GetDB()
    db.execute("INSERT INTO Reviews(user_id, date, title, rating, review) VALUES (?, ?, ?, ?, ?)",
               (user_id, date, title, rating, review))
    db.commit()
    db.close()

    return True

def DeleteReview(user_id, review_id):
    print(f"DeleteReview called with user_id: {user_id}, review_id: {review_id}")
    # Connect to the database
    db = GetDB()

    # Check if the review exists and belongs to the user
    review = db.execute("SELECT * FROM Reviews WHERE id = ? AND user_id = ?", (review_id, user_id)).fetchone()

    if review is None:
        # Review does not exist or does not belong to the user
        print("Review not found or does not belong to the user.")
        return False

    # Delete the review
    db.execute("DELETE FROM Reviews WHERE id = ?", (review_id,))
    db.commit()
    db.close()
    print("Review deleted from database.")
    return True

def EditReview(user_id, review_id, date, title, rating, review):
    # Check if any boxes were empty
    if date is None or title is None or review is None:
        return False

    # Validate rating
    rating = int(rating)
    if rating < 1 or rating > 5:
        return False

    # Get the DB and update the review
    db = GetDB()
    db.execute("""UPDATE Reviews 
                  SET date = ?, title = ?, rating = ?, review = ? 
                  WHERE id = ? AND user_id = ?""",
               (date, title, rating, review, review_id, user_id))
    db.commit()
    db.close()

    return True

def SearchReviews(query):
    db = GetDB()
    reviews = db.execute("""SELECT Reviews.date, Reviews.title, Reviews.rating, Reviews.review, Users.username, Reviews.id
                            FROM Reviews JOIN Users ON Reviews.user_id = Users.id
                            WHERE Users.username LIKE ? OR Reviews.title LIKE ?  
                            ORDER BY Reviews.date DESC, Reviews.id DESC""", ('%' + query + '%', '%' + query + '%')).fetchall() # Displays all reviews where theres a match from the inputed search and the user name/ title
    db.close()
    return reviews

def DeleteAccount(username, password):
    db = GetDB()
    
    # Verify the username and password
    user = db.execute("SELECT * FROM Users WHERE username=?", (username,)).fetchone()
    if user is None or not check_password_hash(user['password'], password):
        return False

    user_id = user['id']
    
    # Delete all reviews by the user
    db.execute("DELETE FROM Reviews WHERE user_id = ?", (user_id,))
    
    # Delete the user account
    db.execute("DELETE FROM Users WHERE id = ?", (user_id,))
    
    db.commit()
    db.close()
    
    return True