"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)
@app.route('/game')
def show_madlib_form():
    #get the users response to a yes or no qestion
    #on "would you like to play a game"

    #if they say no, return a rendered template goodbye.html

    #if yes render templat game.html
    #form should have action = /madlib

@app.route('/madlib')
def show_madlib():
    # show rendered template madlib.html
    """There once was a {{ color }} {{ noun }} sitting in the Hackbright Lab.
    When {{ person }} went to pick it up, it burst into flames in a totally
    {{ adjective }} way."""


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
