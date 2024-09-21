from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    species = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    pets = Pet.query.all()
    return render_template('view_pets.html', pets=pets)

def add_sample_data():
    # Check if the table is empty before adding sample data
    if Pet.query.count() == 0:
        sample_pets = [
            Pet(name='Buddy', age=3, species='Dog'),
            Pet(name='Mittens', age=2, species='Cat'),
            Pet(name='Goldie', age=1, species='Fish'),
        ]
        db.session.bulk_save_objects(sample_pets)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Drops all tables
        db.create_all()  # Creates tables again
        add_sample_data()  # Add sample pets
    app.run(debug=True)
