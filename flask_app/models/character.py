from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

DATABASE = 'ffxiv_builder_schema'


class Character:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.character_id = db_data['character_id']
        self.character_name = db_data['character_name']
        self.character_race = db_data['character_race']
        self.character_title = db_data['character_title']
        self.character_bio = db_data['character_bio']
        self.character_job = db_data['character_job']
        self.character_class = db_data['character_class']
        self.character_free_company = db_data['character_free_company']
        self.character_data_center = db_data['character_data_center']
        self.character_server = db_data['character_server']
        self.character_portrait_url = db_data['character_portrait_url']
        self.character_avatar_url = db_data['character_avatar_url']
        self.class_icon_url = db_data['class_icon_url']
        self.job_icon_url = db_data['class_icon_url']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO characters (character_id, character_name, character_race, character_title, character_bio, character_job, character_class, character_free_company, character_data_center, character_server, character_portrait_url, character_avatar_url, class_icon_url, job_icon_url) VALUES (%(character_id)s, %(character_name)s, %(character_race)s, %(character_title)s, %(character_bio)s, %(character_job)s, %(character_class)s, %(character_free_company)s, %(character_data_center)s, %(character_server)s, %(character_portrait_url)s, %(character_avatar_url)s, %(class_icon_url)s, %(job_icon_url)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
