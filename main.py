from flask import Flask
from flask import request
from flask import render_template
from flask import redirect,url_for
import sqlite3

app = Flask(__name__)

qdict = {}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/new_session")
def create_session():
    global qdict
    # Adding record into Session table
    db = sqlite3.connect('db/sessions.sqlite')
    db.execute('INSERT INTO Session VALUES (NULL,\"\")')
    db.commit()
    # Fetching Session id
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Session ORDER BY id DESC LIMIT 1')
    session = cursor.fetchone()
    # Asking first question
    a = Albot(session[0],db,qdict)
    a.ask('parameter') # First question on most variable parameter
    db.close()
    # redirecting in new session
    return redirect(url_for('chatbox',id=int(session[0])))


@app.route("/session/<id>")
def chatbox(session_id):
    global qdict
    # Rendering conversation
    msg = []
    db = sqlite3.connect('db/sessions.sqlite')
    cursor = db.cursor()
    rows = cursor.execute('SELECT question,answer FROM Session_Step WHERE session_id = ' + str(int(session_id)))
    if cursor.rowcount() > 0:
        for row in rows: # Fetching messages
            msg += {"author":"al.bot","content":row[0]}
            if row[1] is not "":
                msg += {"author":"user","content":row[1]}
    else: # Error
        pass
    # Check if over
    over,answer = state(session_id)
    if over:
        pass # Print answer in template
    db.close()
    return render_template('session.html',messages=msg,session_id=id)


@app.route("/send/<session_id>",methods=['POST'])
def interact(session_id):
    global qdict
    # Getting message
    message = request.form.get('message')
    db = sqlite3.connect('db/sessions.sqlite')
    # Creating bot
    albot = create_bot(db,qdict,session_id)
    # Interacting with user
    albot.interact(message)
    # Returning to chatbox
    return redirect(url_for('chatbox',id=session_id))
