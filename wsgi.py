from app.routes import app
from app import app, db
from app.models import User, Posts, WordsModel

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Posts': Posts, 'WordsModel': WordsModel}
