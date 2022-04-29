import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import character
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
        self.party_members = []
        self.light_party_members = []
        User.all_users.append(self)

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( username, email, password, created_at, updated_at ) VALUES ( %(username)s, %(email)s, %(password)s, NOW(), NOW());"
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
    def add_character_to_full_party(cls, data):
        query = "INSERT INTO full_parties (user_id, character_id) VALUES(%(user_id)s, %(character_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def find_player_character(cls, data):
        query = "SELECT * FROM characters where user_id = users.id;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return

    @classmethod
    def get_full_party_info(cls, data):
        query = "SELECT * FROM users LEFT JOIN full_parties ON users.id = full_parties.user_id LEFT JOIN characters ON characters.id = full_parties.character_id WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        user = cls(results[0])

        for row in results:
            if row['characters.id'] == None:
                break

            data = {
                "id": row['characters.id'],
                "character_id": row['character_id'],
                "character_name": row['character_name'],
                "character_race": row['character_race'],
                "character_title": row['character_title'],
                "character_bio": row['character_bio'],
                "character_job": row['character_job'],
                "character_class": row['character_class'],
                "character_free_company": row['character_free_company'],
                "character_data_center": row['character_data_center'],
                "character_server": row['character_server'],
                "character_portrait_url": row['character_portrait_url'],
                "character_avatar_url": row['character_avatar_url'],
                "class_icon_url": row['class_icon_url'],
                "job_icon_url": row['job_icon_url'],
            }

            user.party_members.append(character.Character(data))
        return user

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

    @classmethod
    def check_user_party_size(cls, data):
        query = "SELECT * from USERS LEFT JOIN full_parties ON users.id = full_parties.character_id LEFT JOIN characters ON characters.id = user_id WHERE users.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        return results

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
