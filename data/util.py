from typing import NoReturn

import streamlit as st
from sqlalchemy import text
from streamlit.connections import SQLConnection

CONNECTION_NAME = "sqlite-db"
DB_URL = "sqlite:///data/data.sqlite"
VALID_TABLE_NAMES = [
    "user",
    "message",
    "user_rating",
    "kitchen",
    "kitchen_image",
    "kitchen_rating",
    "invoices"
]


def get_connection() -> SQLConnection:
    # Let st.connection handle creating or reusing an existing connection
    return st.connection(
        CONNECTION_NAME,
        url=DB_URL,
        type="sql",
    )


def reset_table(conn: SQLConnection, dataset: str) -> NoReturn | None:
    if dataset not in VALID_TABLE_NAMES:
        errmsg = f"Invalid dataset name. Must choose from: {
            ', '.join(VALID_TABLE_NAMES)}"
        raise RuntimeError(errmsg)

    match dataset:
        case "user":
            with conn.session as s:
                s.execute(
                    "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, firstName TEXT, lastName TEXT, email TEXT, age INTEGER, user_type INTEGER NOT NULL);")
                s.execute("DELETE FROM user;")
                users = [
                    {"firstName": "John", "lastName": "Doe",
                        "email": "test@test.com", "age": 25, "user_type": 1},
                    {"firstName": "Jane", "lastName": "Smith",
                        "email": "cat@cats.com", "age": 30, "user_type": 2},
                    {"firstName": "Alex", "lastName": "Johnson",
                        "email": "alex@alexjohnson.com", "age": 35, "user_type": 3},
                ]
                s.execute(
                    text("INSERT INTO user (firstName, lastName, email, age, user_type) VALUES (:firstName, :lastName, :email, :age, :user_type)"),
                    users,
                )
                s.commit()
        case "message":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS message (
                        id INTEGER PRIMARY KEY,
                        message TEXT,
                        sender_id INTEGER NOT NULL,
                        recipient_id INTEGER NOT NULL,
                        FOREIGN KEY(sender_id) REFERENCES user(id),
                        FOREIGN KEY(recipient_id) REFERENCES user(id)
                    );
                    """
                )
                s.execute("DELETE FROM message;")
                messages = [
                    {"message": "Hello", "sender_id": 1, "recipient_id": 2},
                    {"message": "How are you?", "sender_id": 2, "recipient_id": 1},
                    {"message": "I'm good", "sender_id": 1, "recipient_id": 2},
                ]
                s.execute(
                    text(
                        "INSERT INTO message (message, sender_id, recipient_id) VALUES (:message, :sender_id, :recipient_id)"),
                    messages,
                )
                s.commit()
        case "user_rating":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS user_rating (
                        id INTEGER PRIMARY KEY,
                        review TEXT,
                        rating INTEGER,
                        rated_user_id INTEGER,
                        rating_user_id INTEGER,
                        FOREIGN KEY(rated_user_id) REFERENCES user(id),
                        FOREIGN KEY(rating_user_id) REFERENCES user(id)
                    );
                    """
                )
                s.execute("DELETE FROM user_rating;")
                user_ratings = [
                    {"review": "Great User, easy to work with", "rating": 5,
                        "rated_user_id": 1, "rating_user_id": 2},
                    {"review": "User left a massive mess", "rating": 1,
                        "rated_user_id": 2, "rating_user_id": 1},
                    {"review": None, "rating": 3,
                        "rated_user_id": 1, "rating_user_id": 3},
                ]
                s.execute(
                    text(
                        "INSERT INTO user_rating (review, rating, rated_user_id, rating_user_id) VALUES (:review, :rating, :rated_user_id, :rating_user_id)"),
                    user_ratings,
                )
                s.commit()
        case "kitchen":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS kitchen (
                        id INTEGER PRIMARY KEY,
                        address TEXT,
                        owner_id INTEGER,
                        appliances TEXT,
                        size INTEGER,
                        FOREIGN KEY(owner_id) REFERENCES user(id)
                    );
                    """
                )
                s.execute("DELETE FROM kitchen;")
                properties = [
                    {"address": "123 Main St", "owner_id": 1,
                        "appliances": "toaster, oven", "size": 100},
                    {"address": "456 Elm St", "owner_id": 2,
                        "appliances": "oven, barbecue", "size": 200},
                    {"address": "789 Oak St", "owner_id": 3,
                        "appliances": "Air Fryer, Oven, Steamer", "size": 300},
                ]
                s.execute(
                    text(
                        "INSERT INTO kitchen (address, owner_id, appliances, size) VALUES (:address, :owner_id, :appliances, :size)"),
                    properties,
                )
                s.commit()
        case "kitchen_image":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS kitchen_image (
                        id INTEGER PRIMARY KEY,
                        image_name TEXT,
                        kitchen_id INTEGER,
                        FOREIGN KEY(kitchen_id) REFERENCES kitchen(id)
                    );
                    """
                )
                s.execute("DELETE FROM kitchen_image;")
                images = [
                    {"image_name": "kitchen1.jpg", "kitchen_id": 1},
                    {"image_name": "kitchen2.jpg", "kitchen_id": 1},
                    {"image_name": "kitchen3.jpg", "kitchen_id": 2},
                    {"image_name": "kitchen4.jpg", "kitchen_id": 3},
                ]
                s.execute(
                    text(
                        "INSERT INTO kitchen_image (image_name, kitchen_id) VALUES (:image_name, :kitchen_id)"),
                    images,
                )
                s.commit()
        case "kitchen_rating":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS kitchen_rating (
                        id INTEGER PRIMARY KEY,
                        review TEXT,
                        rating INTEGER,
                        rated_kitchen_id INTEGER,
                        rating_user_id INTEGER,
                        FOREIGN KEY(rated_kitchen_id) REFERENCES kitchen(id),
                        FOREIGN KEY(rating_user_id) REFERENCES user(id)
                    );
                    """
                )
                s.execute("DELETE FROM kitchen_rating;")
                kitchen_ratings = [
                    {"review": "Great Kitchen, easy to use", "rating": 5,
                        "rated_kitchen_id": 1, "rating_user_id": 2},
                    {"review": "Kitchen was a mess", "rating": 1,
                        "rated_kitchen_id": 2, "rating_user_id": 1},
                    {"review": None, "rating": 3,
                        "rated_kitchen_id": 1, "rating_user_id": 3},
                ]
                s.execute(
                    text("INSERT INTO kitchen_rating (review, rating, rated_kitchen_id, rating_user_id) VALUES (:review, :rating, :rated_kitchen_id, :rating_user_id)"),
                    kitchen_ratings,
                )
                s.commit()
        case "invoices":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS invoices (
                        id INTEGER PRIMARY KEY,
                        invoice_number TEXT,
                        invoice_date DATE DEFAULT CURRENT_DATE,
                        amount REAL,
                        user_id INTEGER,
                        FOREIGN KEY(user_id) REFERENCES user(id)
                    );
                    """
                )
                s.execute("DELETE FROM invoices;")
                invoices = [
                    {"invoice_number": "INV-001", "invoice_date": "2022-01-01",
                        "amount": 100.00, "user_id": 1},
                    {"invoice_number": "INV-002", "invoice_date": "2022-01-01",
                        "amount": 200.00, "user_id": 2},
                    {"invoice_number": "INV-003", "invoice_date": "2022-01-02",
                        "amount": 300.00, "user_id": 3},
                ]
                s.execute(
                    text(
                        "INSERT INTO invoices (invoice_number, amount, user_id) VALUES (:invoice_number, :amount, :user_id)"),
                    invoices,
                )
                s.commit()
