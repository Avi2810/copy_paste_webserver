from flask import Flask, render_template, request, url_for, redirect
import sqlite3 as sq

app = Flask(__name__)
c = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z']
id = ''

def incr(id):
    ch = id[0]
    n = int(id[1:])
    n = n+1
    if n == 100:
        n=0
        ch = c[c.index(ch)+1]
    return ch+str(n)


def get_id():
    conn = sq.connect('data.db')
    c = conn.execute("SELECT ID FROM DATATABLE ORDER BY IND DESC LIMIT 1")
    try:
        c = c.fetchone()[0]
        conn.close()
        return incr(c)
    except:
        conn.close()
        return "A0"
    


def store_data(id,data):
    conn = sq.connect('data.db')
    conn.execute(" INSERT INTO DATATABLE(ID,DATA) VALUES(?,?)",(id,data))
    conn.commit()
    conn.close()

def get_data(id):
    conn = sq.connect('data.db')
    cursor = conn.execute(" SELECT DATA FROM DATATABLE WHERE ID='"+id+"'")
    cursor = cursor.fetchone()[0]
    conn.close()
    return cursor


@app.route("/", methods=['GET','POST'])
def index():
    id = get_id()
    if request.method == "POST":
        data = request.form["text"]
        store_data(id,data)
        return redirect(url_for('register',id=id))
    return render_template("index.html",id=id)


@app.route("/post-><id>")
def register(id):
    data = get_data(id)
    return render_template("show.html",title=id, id=id ,data=data)


app.run(debug=True)