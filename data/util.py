from io import BytesIO
from PIL import Image
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
    "kitchen_availability",
    "fiscal_transaction",
]


def get_connection() -> SQLConnection:
    # Let st.connection handle creating or reusing an existing connection
    return st.connection(
        CONNECTION_NAME,
        url=DB_URL,
        type="sql",
    )


def showResults(results_df, search_query):
    num_rows_found = len(results_df)
    st.write(f'{num_rows_found} row{"" if num_rows_found ==
                                    1 else "s"} found for `{search_query}`')
    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True,
    )


def showResultsWImages(results_df, search_query):
    num_rows_found = len(results_df)
    st.write(f'{num_rows_found} row{"" if num_rows_found ==
                                    1 else "s"} found for `{search_query}`')
    st.dataframe(
        results_df,
        use_container_width=True,
        hide_index=True,
    )
    conn = get_connection()
    for _, row in results_df.iterrows():
        kitchen_id = row['id']
        image_results = conn.query(
            'SELECT image FROM kitchen_image WHERE kitchen_id = :kitchen_id',
            params=dict(kitchen_id=kitchen_id),
            ttl=0,
        )
        if not image_results.empty:
            images = []

            for _, image_row in image_results.iterrows():
                image_data = image_row['image']
                image_io = BytesIO(image_data)
                image = Image.open(image_io)
                images.append(image)
            st.image(images, caption=[
                     "Kitchen_ID: " + str(kitchen_id)] * len(images))


def recreate_table(conn: SQLConnection, dataset: str) -> NoReturn | None:
    if dataset not in VALID_TABLE_NAMES:
        errmsg = f"Invalid dataset name. Must choose from: {
            ', '.join(VALID_TABLE_NAMES)}"
        raise RuntimeError(errmsg)

    match dataset:
        case "user":
            with conn.session as s:
                s.execute("DROP TABLE IF EXISTS user;")
                s.commit()
            reset_table(conn, "user")
        case "message":
            with conn.session as s:
                s.execute("DROP TABLE IF EXISTS message;")
                s.commit()
            reset_table(conn, "message")
        case "user_rating":
            with conn.session as s:
                s.execute("DROP TABLE IF EXISTS user_rating;")
                s.commit()
            reset_table(conn, "user_rating")
        case "kitchen":
            with conn.session as s:
                s.execute("DROP TABLE IF EXISTS kitchen;")
                s.commit()
            reset_table(conn, "kitchen")
        case "kitchen_availability":
            with conn.session as s:
                s.execute("DROP TABLE IF EXISTS kitchen_availability;")
                s.commit()
            reset_table(conn, "kitchen_availability")
        case "kitchen_image":
            with conn.session as s:
                s.execute("DROP TABLE IF EXISTS kitchen_image;")
                s.commit()
            reset_table(conn, "kitchen_image")
        case "kitchen_rating":
            with conn.session as s:
                s.execute("DROP TABLE IF EXISTS kitchen_rating;")
                s.commit()
            reset_table(conn, "kitchen_rating")
        case "fiscal_transaction":
            with conn.session as s:
                s.execute("DROP TABLE IF EXISTS fiscal_transaction;")
                s.commit()
            reset_table(conn, "fiscal_transaction")


def reset_table(conn: SQLConnection, dataset: str) -> NoReturn | None:
    if dataset not in VALID_TABLE_NAMES:
        errmsg = f"Invalid dataset name. Must choose from: {
            ', '.join(VALID_TABLE_NAMES)}"
        raise RuntimeError(errmsg)

    match dataset:
        case "user":
            with conn.session as s:
                s.execute(
                    """CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY,
                        firstName TEXT, 
                        lastName TEXT, 
                        email TEXT,
                        bank_number TEXT, 
                        age INTEGER,
                        auto_payments BOOLEAN DEFAULT FALSE, 
                        user_type INTEGER NOT NULL
                    );
                    """
                )
                s.execute("DELETE FROM user;")
                users = [
                    {"firstName": "John", "lastName": "Doe",
                        "email": "test@test.com", "bank_number": "1234-5678-9101-1121", "age": 25, "user_type": 1},
                    {"firstName": "Jane", "lastName": "Smith",
                        "email": "cat@cats.com", "bank_number": "1234-5678-9101-1122", "age": 30, "user_type": 2},
                    {"firstName": "Alex", "lastName": "Johnson",
                        "email": "alex@alexjohnson.com", "bank_number": "1234-5678-9101-1123", "age": 35, "user_type": 3},
                ]
                s.execute(
                    text("INSERT INTO user (firstName, lastName, email, bank_number, age, user_type) VALUES (:firstName, :lastName, :email, :bank_number, :age, :user_type)"),
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
                        name TEXT,
                        pricing TEXT,
                        address TEXT,
                        owner_id INTEGER,
                        appliances TEXT,
                        description TEXT,
                        FOREIGN KEY(owner_id) REFERENCES user(id)
                    );                    
                    """
                )
                s.execute("DELETE FROM kitchen;")
                properties = [
                    {"name": "Happy Kitchen", "pricing": "$10 an hour", "address": "123 Main St", "owner_id": 1,
                        "appliances": "toaster, oven", "description": "A happy kitchen"},
                    {"name": "Sad Kitchen", "pricing": "$10 an hour", "address": "456 Elm St", "owner_id": 2,
                        "appliances": "oven, barbecue", "description": "A sad kitchen"},
                    {"name": "Indifferent Kitchen", "pricing": "$10 an hour", "address": "789 Oak St", "owner_id": 3,
                        "appliances": "Air Fryer, Oven, Steamer", "description": "An indifferent kitchen"},
                ]
                s.execute(
                    text(
                        "INSERT INTO kitchen (name, pricing, address, owner_id, appliances, description) VALUES (:name, :pricing, :address, :owner_id, :appliances, :description)"),
                    properties,
                )
                s.commit()
        case "kitchen_availability":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS kitchen_availability (
                        id INTEGER PRIMARY KEY,
                        kitchen_id INTEGER,
                        start_date DATE,
                        end_date DATE,
                        FOREIGN KEY(kitchen_id) REFERENCES kitchen(id)
                    );                    
                    """
                )
                s.execute("DELETE FROM kitchen_availability;")
                properties = [
                    {"kitchen_id": 1, "start_date": "2022-01-01",
                        "end_date": "2022-01-02"},
                    {"kitchen_id": 2, "start_date": "2022-01-01",
                        "end_date": "2022-01-02"},
                    {"kitchen_id": 3, "start_date": "2022-01-01",
                        "end_date": "2022-01-02"},
                ]
                s.execute(
                    text(
                        "INSERT INTO kitchen_availability (kitchen_id, start_date, end_date) VALUES (:kitchen_id, :start_date, :end_date)"),
                    properties,
                )
                s.commit()
        case "kitchen_image":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS kitchen_image (
                        id INTEGER PRIMARY KEY,
                        image BLOB,
                        kitchen_id INTEGER,
                        FOREIGN KEY(kitchen_id) REFERENCES kitchen(id)
                    );
                    """
                )
                s.execute("DELETE FROM kitchen_image;")
                # images = [
                #     {"image": "kitchen1", "kitchen_id": 1},
                #     {"image": "kitchen2", "kitchen_id": 1},
                #     {"image": "kitchen3", "kitchen_id": 2},
                #     {"image": "kitchen4", "kitchen_id": 3},
                # ]
                # s.execute(
                #     text(
                #         "INSERT INTO kitchen_image (image, kitchen_id) VALUES (:image, :kitchen_id)"),
                #     images,
                # )
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
        case "fiscal_transaction":
            with conn.session as s:
                s.execute(
                    """
                    CREATE TABLE IF NOT EXISTS fiscal_transaction (
                        id INTEGER PRIMARY KEY,
                        transaction_date DATE DEFAULT CURRENT_DATE,
                        amount REAL,
                        payor_user_id INTEGER,
                        payee_user_id INTEGER,
                        FOREIGN KEY(payor_user_id) REFERENCES user(id)
                        FOREIGN KEY(payee_user_id) REFERENCES user(id)
                    );
                    """
                )
                s.execute("DELETE FROM fiscal_transaction;")
                transactions = [
                    {"amount": 100.00, "payor_user_id": 1, "payee_user_id": 2},
                    {"amount": 200.00, "payor_user_id": 2, "payee_user_id": 3},
                    {"amount": 300.00, "payor_user_id": 3, "payee_user_id": 1},
                ]
                s.execute(
                    text(
                        "INSERT INTO fiscal_transaction (amount, payor_user_id, payee_user_id) VALUES (:amount, :payor_user_id, :payee_user_id)"),
                    transactions,
                )
                s.commit()
