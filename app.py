from apps import app
import flask_cors


flask_cors.CORS(app, resources=r'/*')
if __name__ == '__main__':
    app.run()
