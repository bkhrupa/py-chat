import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf.csrf import CSRFProtect

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database/database.sqlite')
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)
db.init_app(app)

csrf = CSRFProtect()
csrf.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(255))

    def __repr__(self):
        return '<User %r>' % self.id


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.id


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message_text = request.form['message']

        if len(message_text) > 0:
            message = Message(message=message_text)

            try:
                db.session.add(message)
                db.session.commit()
            except:
                return 'Something went wrong in message'

        return redirect(url_for('chat'))
    else:
        messages = Message.query.order_by(Message.id.desc()).limit(50).all()

        return render_template('chat.html', messages=messages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
