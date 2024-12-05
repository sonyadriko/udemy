from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(_name_)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://todo.db"
db = SQLAlchemy(app)

class Todo(db.Model)
    sno = db.Column(db.Integer, primary_key=true)
    title = db.Column(db.String(200), nullable=false)
    desc = db.Column(db.String(200), nullable=false)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    
    def _repr_(self) -> str:
        return f"{self.sno}" - {self.title}