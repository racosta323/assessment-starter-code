from flask import request, make_response
from config import app, db, api
from models import Project
from flask_restful import Resource

import ipdb

class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        project_list = [project.to_dict() for project in projects]
        return make_response(project_list, 200)
    
    def post(self):
        request_body = request.json

        project = Project(
            name = request_body['name'],
            about = request_body['about'],
            phase = request_body['phase'],
            link = request_body['link'],
            image = request_body['image']
        )

        db.session.add(project)
        db.session.commit()

        return make_response(project.to_dict(), 201)

api.add_resource(Projects, '/projects')

