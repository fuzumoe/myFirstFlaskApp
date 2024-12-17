from app import create_app
from app.routes import register_route


app = create_app()

register_route(app)


if __name__ == "__main__":
    app.run(debug=True)