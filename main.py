from flask import Flask
from flask import request
from flask import render_template
from flask import redirect,url_for
import sqlite3
import Qdict
from chatbot.Albot import Albot,create_bot,state
from chatbot.QDict import QDict

app = Flask(__name__)

qdict = QDict(Qdict.get_qdict())

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/new_session")
def create_session():
    global qdict
    # Adding record into Session table
    db = sqlite3.connect('db/sessions.sqlite')
    phone_db = sqlite3.connect('db/phones.sqlite')
    db.execute('INSERT INTO Session VALUES (NULL,\"\")')
    db.commit()
    # Fetching Session id
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Session ORDER BY id DESC LIMIT 1')
    session = cursor.fetchone()
    # Asking first question
    a = Albot(int(session[0]),db,phone_db,qdict)
    a.ask('price') # First question on most variable parameter
    db.close()
    phone_db.close()
    # redirecting in new session
    return redirect(url_for('chatbox',session_id=int(session[0])))


@app.route("/session/<session_id>")
def chatbox(session_id):
    global qdict
    # Rendering conversation
    msg = []
    db = sqlite3.connect('db/sessions.sqlite')
    cursor = db.cursor()
    rows = cursor.execute('SELECT question,answer,qcm FROM Session_Step WHERE session_id = ' + str(int(session_id)))
    for row in rows: # Fetching messages
        msg.append({"author":"al.bot","content":row[0],"qcm":row[2]})
        if row[1] is not "":
            msg.append({"author":"user","content":row[1],"qcm":'0'})
    # Check if over
    over,answer = state(db,session_id)
    if over:
        pass # Print answer in template
    db.close()
    return render_template('session.html',messages=msg,session_id=session_id)


@app.route("/send/<session_id>",methods=['POST'])
def interact(session_id):
    global qdict
    # Getting message
    message = request.form.get('message')
    db = sqlite3.connect('db/sessions.sqlite')
    phone_db = sqlite3.connect('db/phones.sqlite')
    # Creating bot
    albot = create_bot(db,phone_db,qdict,session_id)
    # Interacting with user
    albot.interact(message)
    # Returning to chatbox
    db.close()
    phone_db.close()
    return redirect(url_for('chatbox',session_id=session_id))
