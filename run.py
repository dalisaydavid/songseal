# run.py

from app import app

app.secret_key = 'some secret key'
if __name__ == '__main__':
    app.run()