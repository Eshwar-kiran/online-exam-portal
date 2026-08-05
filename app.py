from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///exam.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------------------- Models ----------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    options = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Question('{self.text}')"


# ---------------------- Questions ----------------------

questions = [
    {
        "text": "What is the capital of France?",
        "options": "Paris,London,Berlin,Rome",
        "answer": "Paris"
    },
    {
        "text": "What is the largest planet in our solar system?",
        "options": "Earth,Jupiter,Saturn,Uranus",
        "answer": "Jupiter"
    },
    {
        "text": "What is the smallest country in the world?",
        "options": "Vatican City,Monaco,Nauru,Tuvalu",
        "answer": "Vatican City"
    },
    {
        "text": "What is the highest mountain in the world?",
        "options": "Mount Everest,K2,Kangchenjunga,Lhotse",
        "answer": "Mount Everest"
    },
    {
        "text": "What is the largest living species of lizard?",
        "options": "Komodo dragon,Saltwater crocodile,Black caiman,American alligator",
        "answer": "Komodo dragon"
    }
]


# ---------------------- Database Initialization ----------------------

def init_db():

    db.create_all()

    if Question.query.count() == 0:

        for q in questions:

            db.session.add(
                Question(
                    text=q["text"],
                    options=q["options"],
                    answer=q["answer"]
                )
            )

        db.session.commit()


with app.app_context():
    init_db()


# ---------------------- Routes ----------------------

@app.route("/")
def index():
    message = request.args.get("message")
    return render_template("index.html", message=message)


# ---------------------- Register ----------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:

            return render_template(
                "register.html",
                error="Username already exists."
            )

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(
            url_for(
                "login",
                message="Registration successful! Please login."
            )
        )

    return render_template("register.html")


# ---------------------- Login ----------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id

            return redirect(url_for("exam"))

        else:

            return render_template(
                "login.html",
                error="Invalid username or password."
            )
        
    return render_template("login.html")


# ---------------------- Exam ----------------------

@app.route("/exam")
def exam():

    if "user_id" not in session:

        return redirect(
            url_for(
                "login",
                message="Please login first."
            )
        )

    questions = Question.query.all()

    return render_template(
        "exam.html",
        questions=questions
    )


# ---------------------- Submit ----------------------

@app.route("/submit", methods=["POST"])
def submit():

    if "user_id" not in session:

        return redirect(url_for("login"))

    score = 0

    questions = Question.query.all()

    for question in questions:

        answer = request.form.get(str(question.id))

        if answer == question.answer:

            score += 1

    return render_template(
        "result.html",
        score=score
    )


# ---------------------- Logout ----------------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for(
            "login",
            message="You have been logged out successfully."
        )
    )


# ---------------------- Run ----------------------

if __name__ == "__main__":
    app.run(debug=True, port=5050)