import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
DATABASE = 'ffxiv_builder_schema'


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    all_users = []

    def __init__(self, db_data):
        self.id = db_data['id']
        self.username = db_data['username']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.player_character = []
        self.party_members = []
        User.all_users.append(self)

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( username, email, password, created_at, updated_at ) VALUES (%(username)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        found_user = connectToMySQL(DATABASE).query_db(query, data)[0]
        return cls(found_user)

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users where email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            flash('Invalid email/password.', 'err_user_login')
            return False
        return cls(result[0])

    @classmethod
    def validate_unique_email(cls, data):
        print('Running unique email validation...')
        query = "SELECT * FROM users WHERE users.email = %(email)s"
        amount_of_query = connectToMySQL(DATABASE).query_db(query, data)
        is_valid = True
        if len(amount_of_query) >= 1:
            flash(
                f'An email with this name already exists!', "err_user_email")
            is_valid = False
        return is_valid


    # @classmethod
    # def check_if_user_exists(cls, data):
    #     print("Running user checker...")
    #     query = "SELECT * FROM users WHERE id = %(id)s;"


    @staticmethod
    def validate_email(form_data: dict):
        print('Running email name validation...')
        is_valid = True
        if len(form_data['email']) < 8:
            flash('Email length must be at least 8 characters long!',
                  'err_user_email')
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address!", 'err_user_email')
            is_valid = False
        return is_valid

    @staticmethod
    def validate_password(form_data: dict):
        print('Validating password...')
        is_valid = True
        if len(form_data['password']) < 8:
            flash('Your password must be at least 8 characters long!',
                  'err_user_register_password')
            is_valid = False
        if form_data['password'] != form_data['confirm_pw']:
            flash('The passwords you entered do not match! Please try again.',
                  'err_user_register_password')
            is_valid = False
        return is_valid

    # @classmethod
    # def get_user_with_sighting(cls, data):
    #     query = "SELECT posts.id, users.first_name, users.last_name, description, date_of_sighting, location, num_of_sasquatch FROM posts LEFT JOIN users ON posts.user_id = users.id WHERE posts.id = %(id)s"
    #     results = connectToMySQL(DATABASE).query_db(query, data)[0]
    #     if not results:
    #         return []

    #     # for row in results:
    #     #     if not results:
    #     #         break

    #     #     print(row)
    #     #     data = {
    #     #         "date_of_sighting": row["date_of_sighting"],
    #     #         "description": row["description"],
    #     #         "first_name": row["first_name"],
    #     #         "last_name": row["last_name"],
    #     #         "location": row["location"],
    #     #         "num_of_sasquatch": row["num_of_sasquatch"]
    #     #     }
    #     #     User.posts.append(data)
    #     # print(type(results))
    #     return results
