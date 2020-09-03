from flask import Flask, request, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddNewPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:postgres4@localhost/pets'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_home():
    pets = Pet.query.all()
    return render_template('home.html', pets = pets)

@app.route('/add', methods=["POST", "GET"])
def show_add_pet_form():
    form = AddNewPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = bool(form.available.data)
        if photo_url == "":
            photo_url = "https://secure.gravatar.com/avatar/a97703cbfea6a0ccee000eefa1cde37a?s=256&d=mm&r=g"
        pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes, available = available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add-pet.html', form = form)

@app.route('/<int:pet_id>', methods=["POST", "GET"])
def show_edit_pet_form(pet_id):
    pet = Pet.query.get(pet_id)
    form = AddNewPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = bool(form.available.data)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit-pet.html', form = form)