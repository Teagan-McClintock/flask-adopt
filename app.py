"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def show_homepage():
    """Displays homepage listing pets with their photos and adoption status.
    Contains link to form to add a new pet."""

    pets = Pet.query.order_by(Pet.id).all()

    return render_template("homepage.html", pets=pets)

@app.route("/add", methods=["GET","POST"])
def add_pet():
    """Display add pet form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data,
       )

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("pet_add_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET","POST"])
def show_pet_profile(pet_id):
    """Pet's profile page with pet's name, photo, age, species,
    also handles edit form."""

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data,
        pet.notes = form.notes.data,
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        return redirect(f"/{pet.id}")

    else :
        return render_template("pet_profile.html", form=form, pet=pet)








