from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reindeer_games.db'
db = SQLAlchemy(app)


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    past_partners = db.Column(db.String)
    reindeer_games_won = db.Column(db.Integer)

    # Method that returns list of previous partners
    # Method that increments score by passed amount
    # Method that increments player partners
    # Method that deletes player
    # Method that resets player score
    # Method that clears player previous partners

    def __repr__(self):
        return '<Player %r>' % self.name


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    team_size = db.Column(db.Integer, nullable=False)
    first_place = db.Column(db.Integer)
    second_place = db.Column(db.Integer)
    third_place = db.Column(db.Integer)

    # Create method to determine point values for 1st-3rd depending on team size (singles, doubles, or larger groups etc

    def __repr__(self):
        return '<Game %r>' % self.name


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    if request.method == 'POST':
        player_name = request.form['player_name']
        new_player = Player(name=player_name, score=0, rank=1)

        try:
            db.session.add(new_player)
            db.session.commit()
            return redirect('/')

        except:
            return 'There was an issue adding this player'
    else:
        players = Player.query.order_by(Player.rank).all()
        return render_template('index.html', players=players)


if __name__ == '__main__':
    app.run(debug=True)
