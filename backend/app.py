from flask import Flask, render_template, request, redirect, flash
from database import db
from models import Controller, Flight, Task

def create_app():

    app = Flask(__name__)

    app.secret_key = "atc-secret-key"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///atc.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app

app = create_app()

@app.route("/")
def home():

    controllers = Controller.query.all()

    flights = Flight.query.all()

    tasks = Task.query.all()


    return render_template(
        "dashboard.html",
        controllers=controllers,
        flights=flights,
        tasks=tasks
    )

@app.route("/controllers")
def controllers_page():

    controllers = Controller.query.all()

    return render_template(
        "controllers.html",
        controllers=controllers
    )

@app.route("/flights")
def flights_page():

    flights = Flight.query.all()

    return render_template(
        "flights.html",
        flights=flights
    )

@app.route("/tasks/create", methods=["POST"])
def create_task():

    title = request.form["title"]

    priority = request.form["priority"]

    status = request.form["status"]

    flight_id = request.form["flight_id"]

    controller_id = request.form["controller_id"]


    task = Task(
        title=title,
        priority=priority,
        status=status,
        flight_id=flight_id,
        controller_id=controller_id
    )


    db.session.add(task)

    db.session.commit()

    flash("Task created successfully!")

    return redirect("/")

@app.route("/tasks/delete/<int:id>")
def delete_task(id):

    task = Task.query.get(id)


    if task:

        db.session.delete(task)

        db.session.commit()

        flash("Task deleted!")

    return redirect("/")

@app.route("/tasks/status/<int:id>/<status>")
def update_status(id, status):

    task = Task.query.get(id)


    if task:

        task.status = status

        db.session.commit()


    return redirect("/")

@app.route("/init-db")
def init_db():

    db.create_all()


    controller = Controller(
        name="Alex Popescu",
        sector="Bucharest ACC",
        role="ATC Controller"
    )


    flight = Flight(
        flight_number="RO301",
        aircraft="B737",
        departure="OTP",
        destination="LHR",
        status="ACTIVE"
    )


    task = Task(
        title="Verify landing clearance",
        priority="HIGH",
        status="PENDING",
        controller=controller,
        flight=flight
    )


    db.session.add(controller)
    db.session.add(flight)
    db.session.add(task)


    db.session.commit()

    flash("Task status updated!")

    return redirect("/")


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
