from flask import Flask, request, jsonify
from database import get_db
from schemas import UserCreate, UserRead, ProductCreate, ProductRead, OrderCreate, OrderRead
from crud import create_user, get_user, create_product, get_product, create_order, get_order
from sqlalchemy.orm import Session

def register_routes(app: Flask):
    @app.post("/users/")
    def create_user_route():
        db: Session = next(get_db())
        user_data = UserCreate(**request.json)
        user = create_user(db, user_data)
        return jsonify(UserRead.from_orm(user))

    @app.get("/users/<int:user_id>/")
    def read_user_route(user_id: int):
        db: Session = next(get_db())
        user = get_user(db, user_id)
        return jsonify(UserRead.from_orm(user))

    @app.post("/products/")
    def create_product_route():
        db: Session = next(get_db())
        product_data = ProductCreate(**request.json)
        product = create_product(db, product_data)
        return jsonify(ProductRead.from_orm(product))

    @app.get("/products/<int:product_id>/")
    def read_product_route(product_id: int):
        db: Session = next(get_db())
        product = get_product(db, product_id)
        return jsonify(ProductRead.from_orm(product))

    @app.post("/orders/")
    def create_order_route():
        db: Session = next(get_db())
        order_data = OrderCreate(**request.json)
        order = create_order(db, order_data)
        return jsonify(OrderRead.from_orm(order))

    @app.get("/orders/<int:order_id>/")
    def read_order_route(order_id: int):
        db: Session = next(get_db())
        order = get_order(db, order_id)
        return jsonify(OrderRead.from_orm(order))
