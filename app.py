#!/usr/bin/env python3 
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
#from werkzeug.security import generate_password_hash, check_password_hash
#from functools import wraps
import sqlite3
from mydatabase import init_db

## VAR FOR "suffisait_de_demander"
app = Flask(__name__, template_folder='./templates')


###################################################################################################################################
#                                                Initialization of the database                                                   #  
#                                                                                                                                 #
###################################################################################################################################

init_db()

member_temp_db = {
                    "0" : "SECRET.txt",
                    "1" : "member1.txt",
                    "2" : "member2.txt",
                    "3" : "member3.txt",}
@app.route("/")
def index():
    return render_template("index.html")
    
@app.route('/member_info')
def member_info():
    # Get member_id from GET parameters
    member_id = request.args.get('id', type=str)

    # Check if member_id exists in member_temp_db
    if member_id in member_temp_db:
        fiche = member_temp_db[member_id]
        return send_from_directory('static/members', fiche)
    else:
        return "Member not found", 404
    
    
###################################################################################################################################
#                                     THESE FUNCTIONS ARE USED IN THE SQL AND USER AGENT CHALLENGES                               #  
#                                                                                                                                 #
###################################################################################################################################
def check_ip_provenance(operations=False):
    UA = request.headers.get('User-Agent')
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        addr = request.environ['REMOTE_ADDR']
    else:
        addr = request.environ['HTTP_X_FORWARDED_FOR'].split('.')
    return ((addr[0], addr[1]) == ('192','168') and ( "XSS_SUPER_NAV" in UA.upper() or not operations))

def check_sql_input(s):
    filtered = ["INSERT","UPDATE","DELETE","DROP","ALTER","TRUNCATE","EXEC","EXECUTE","OR","AND","CREATE",
                "GRANT","REVOKE","XP_CMDSHELL","SHUTDOWN","MERGE","LIKE","LOAD DATA","="," "]
    for keyword in filtered:
        if keyword in s.upper():
            print(f"KEYWORD DETECTED : {keyword}")
            return False
    return True



@app.route('/operations-3198102432DDA')
def operations():
    s = request.args.get('search', default="0")
    con = sqlite3.connect("agents.db")
    cur = con.cursor()
    if check_ip_provenance(operations=True):
        try: # the try - except block is used to fetch the data from the DB 
            if check_sql_input(s): 
                if s == "0":
                    cur.execute("SELECT title,descriptions,associated_agents FROM missions")
                else:
                    cur.execute(f"SELECT title, descriptions, associated_agents FROM missions WHERE associated_agents LIKE '%{s}%'")
            else:
                return render_template("operations-3198102432DDA.html", alert="Malicious keyword detected")
            data = cur.fetchall()
        except sqlite3.Error as error:
            data = error
            return str(data), 500
        # once the data is fetched we render it inside the page
        return render_template('operations-3198102432DDA.html', data=data)
    else: # if the ip doesn't match the admin's one don't give access to the page
        return render_template("restricted.html", operations=True)


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
