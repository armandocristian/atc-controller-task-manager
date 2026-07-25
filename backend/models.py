from database import db


class Controller(db.Model):

    __tablename__ = "controllers"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    sector = db.Column(
        db.String(100),
        nullable=False
    )


    role = db.Column(
        db.String(50),
        nullable=False
    )


    tasks = db.relationship(
        "Task",
        backref="controller"
    )



class Flight(db.Model):

    __tablename__ = "flights"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    flight_number = db.Column(
        db.String(20),
        nullable=False
    )


    aircraft = db.Column(
        db.String(50)
    )


    departure = db.Column(
        db.String(50)
    )


    destination = db.Column(
        db.String(50)
    )


    status = db.Column(
        db.String(50)
    )


    tasks = db.relationship(
        "Task",
        backref="flight"
    )



class Task(db.Model):

    __tablename__ = "tasks"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    title = db.Column(
        db.String(200),
        nullable=False
    )


    priority = db.Column(
        db.String(20)
    )


    status = db.Column(
        db.String(30)
    )


    flight_id = db.Column(
        db.Integer,
        db.ForeignKey("flights.id")
    )


    controller_id = db.Column(
        db.Integer,
        db.ForeignKey("controllers.id")
    )
