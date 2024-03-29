import os, json

basedir = os.path.abspath(os.path.dirname(__file__))

with open("bilgiler/bilgiler.json") as read_file:
    data = read_file.read()

obj = json.loads(data)

username = obj['username']
password = obj['password']


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://' + username + ':' + password + '@englishdb:5432/englishdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
