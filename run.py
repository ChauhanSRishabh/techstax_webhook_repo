from flask.helpers import make_response
from api import *
from api import create_app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)