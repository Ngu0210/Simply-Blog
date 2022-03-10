import os
from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://postgres:{os.getenv('DBPASS')}@23.22.149.187:5432/simply_blog"
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    db = SQLAlchemy(app)
    return db


# import os
# import psycopg2

# connection = psycopg2.connect(
#         database="simply_blog",
#         user="postgres",
#         password=os.getenv("DBPASS"),
#         host="23.22.149.187",
#         port="5432"
#     )

# cursor = connection.cursor()

# cursor.execute("create table if not exists users (id serial PRIMARY KEY, firstName varchar, lastName varchar);")
# cursor.execute("drop table if exists books;")
# connection.commit()