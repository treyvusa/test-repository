import sqlite3
from flask_restful import Resource, reqparse
from Section_6.models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This argument is required!'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This argument is required!'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        print('username: ', data['username'])
        print('Find by username: ', UserModel.find_by_username(data['username']))

        if UserModel.find_by_username(data['username']):
            return {"message": "User '{}' already exists.".format(data['username'])}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
