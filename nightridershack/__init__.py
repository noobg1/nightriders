from flask import Flask


app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'jeevu.g1@gmail.com'
app.config["MAIL_PASSWORD"] = '105522114'

from routes import mail
mail.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:commonpassword@localhost/nightriders'

from models import db
db.init_app(app)

import nightridershack.routes
