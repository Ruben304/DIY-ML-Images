from flask import request, jsonify
from app import app, db
from app.models import Project, User

# POST = create
# GET = retrieve
# PUT = replace
# DELETE = delete
# PATCH = update

# create  a project
@app.route('/create_project', methods=['POST'])
def create_project():
    data = request.json

    new_project = Project(name= data['name'], user_id= data['user_id'], status= ['status'], project_type= ['project_type'])

    # add user to the db session and commit
    db.session.add(new_project)
    db.session.commit()

    # success message
    return jsonify({'message': 'Project created successfully'}), 201

# create a user 
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json

    # check username unique
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    # create a new username
    new_user = User(username=data['username'])

    # add user to the db session and commit
    db.session.add(new_user)
    db.session.commit()

    # success message
    return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201

# get a specific project info
@app.route('/project/<int:project_id>', methods=['GET'])
def get_project(project_id):
    # query db for the project with project_ID
    project = Project.query.get(project_id)
    
    # error if it dosent exist
    if not project:
        return jsonify({'message': 'Project not found'}), 404

    # exsit then return info
    project_data = {
        'id': project.id,
        'name': project.name,
        'user_id': project.user_id,
        'status': project.status,
        'project_type': project.project_type
    }

    return jsonify(project_data), 200

# get all project info 
@app.route('/projects', methods=['GET'])
def list_projects():
    projects = Project.query.all()  # fetch all project instances in db
    projects_data = [{
        'id': project.id,
        'name': project.name,
        'user_id': project.user_id,
        'status': project.status,
        'project_type': project.project_type
    } for project in projects]  # create a list of the details

    return jsonify(projects_data), 200

# get all the project related to a specific user 
@app.route('/user/projects', methods=['GET'])
def list_user_projects(current_user):
    projects = Project.query.filter_by(user_id=current_user.id).all()  # get projects from user
    projects_data = [{
        'id': project.id,
        'name': project.name,
        'user_id': project.user_id,
        'status': project.status,
        'project_type': project.project_type
    } for project in projects]  # create list of project details

    return jsonify(projects_data), 200

# get all users info 
@app.route('/users', methods=['GET'])
def list_projects():
    users = User.query.all()  # fetch all users instances in db
    users_data = [{
        'id': user.id,
        'username': user.name,
        'projects': user.projects
    } for user in users]  # create a list of the details

    return jsonify(users_data), 200

# get info of specific user 
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    user_info = {
        'id': user.id,
        'username': user.username,
        'projects': user.projects
    }

    return jsonify(user_info), 200