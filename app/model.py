from app import db


# create custom objects for both projects and users 

# instances of projects correspond to rows on a table
# keys link relationships
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True) # creates a column for ids, and marked as primary key to identify row
    name = db.Column(db.String(128), nullable=False) # creates a column for names, stores up to 128 char and cant be empty
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # creates a column for user_id to linnk project to users, and project must be associated with users
    status = db.Column(db.String(128), nullable=False) # creates a column for the status of project, andn cant be empty
    project_type = db.Column(db.String(128), nullable=False) # creates a column of project being image or object

# similar to project 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # user id
    username = db.Column(db.String(128), unique=True, nullable=False) # username and ensures uniqueness
    projects = db.relationship('Project', backref='user', lazy=True) # creates association of User and Projects, and lazy=True allows projects association to be lister