import datetime
from selenium_insta import time_helper
from selenium_insta.db_handler import *
from selenium_insta import constants


# delete user by name
def delete_user(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    sql = "DELETE FROM followed_users WHERE username = '{0}'".format(username)
    cursor.execute(sql)
    mydb.commit()


# new user
def add_user(username):
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username,date_added) VALUES(%s,%s)", (username, now))
    mydb.commit()

#ready to unfollow
def check_unfollow_list():
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    users_to_unfollow = []
    for r in results:
        d = time_helper.days_since_date(r[1])
        if d < constants.DAYS_TO_UNFOLLOW:
            users_to_unfollow.append(r[0])
        return users_to_unfollow

#get all
def get_followed_users():
    users = []
    mydb = DBHandler.get_mydb()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    for r in results:
        users.append(r[0])
    return users