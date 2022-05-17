"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SECRET_KEY'] = "abcd1234"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 Error Page
    """
    return render_template('404.html'), 404


@app.route("/")
def homepage():
    """
    List of cupcakes
    """
    return render_template("home.html")


@app.route("/api/cupcakes")
def get_list_cupcakes():
    """
    Get data about all cupcakes.
    Respond with JSON like: {cupcakes: [{id, flavor, size, rating, image}, ...]}.
    The values should come from each cupcake instance.
    """

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake_details(cupcake_id):
    """
    Get data about a single cupcake.
    Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
    This should raise a 404 if the cupcake cannot be found.
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """
    Create a cupcake with flavor, size, rating and image data from the body of the request.
    Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
    """
    flavor_j = request.json["flavor"]
    size_j = request.json["size"]
    rating_j = request.json["rating"]
    image_j = request.json["image"]
    new_cupcake = Cupcake(flavor=flavor_j, size=size_j, rating=rating_j, image=image_j)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """
    Update a cupcake with the id passed in the URL and flavor, size, rating and image data from the body of the request. 
    You can always assume that the entire cupcake object will be passed to the backend.
    This should raise a 404 if the cupcake cannot be found.
    Respond with JSON of the newly-updated cupcake, like this: {cupcake: {id, flavor, size, rating, image}}
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """
    This should raise a 404 if the cupcake cannot be found.
    Delete cupcake with the id passed in the URL. Respond with JSON like {message: "Deleted"}.
    """
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
