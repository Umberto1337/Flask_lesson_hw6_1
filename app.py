from flask import Flask
from database import init_db
from routes import register_routes

app = Flask(__name__)

# Инициализация базы данных
init_db()

# Регистрация маршрутов
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
