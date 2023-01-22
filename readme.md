# Py Chat

for study and experiments


## TODO

* Flask-Alembic https://flask-alembic.readthedocs.io/en/stable/


## venv

$ python3 -m venv ~/work/py-chat/venv

$ source ~/work/py-chat/venv/bin/activate

$ pip install -r requirements.txt

$ deactivate

## db

$ flask shell
>>> from app import db, User, Message
>>> db.create_all()

$ flask shell
>>> from app import db, User, Message
>>> db.drop_all()
>>> db.create_all()

$ flask shell
>>> from app import db, User, Message
>>> u = User(nickname='odin')
>>> db.session.add(u)
>>> db.session.commit()


