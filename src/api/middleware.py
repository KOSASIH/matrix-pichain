from flask import request, jsonify

class Middleware:
    def __init__(self, app):
        self.app = app
        self.setup_middleware()

    def setup_middleware(self):
        @self.app.before_request
        def log_request():
            print(f"Request: {request.method} {request.path} - {request.json}")

        @self.app.errorhandler(Exception)
        def handle_exception(e):
            response = {
                "status": "error",
                "message": str(e)
            }
            return jsonify(response), 500

    def __repr__(self):
        return "Middleware()"

# Initialize middleware in the main application
middleware = Middleware(app)
