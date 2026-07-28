import sqlite3


def connect_db():
    return sqlite3.connect("recipe.db")


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    # Create country table first
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS country (
        country_id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_name TEXT NOT NULL UNIQUE
    )
    """)

    # Create recipes table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_name TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        country_id INTEGER NOT NULL,
        FOREIGN KEY (country_id) REFERENCES country(country_id)
    )
    """)

    # Admin table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def country_cuisine():
    """Insert default cuisines only if they don't already exist."""

    conn = connect_db()
    cursor = conn.cursor()

    countries = [
        ("Malaysian",),
        ("French",),
        ("Italian",),
        ("Japanese",),
        ("Chinese",),
        ("American",),
        ("Indonesian",)
    ]

    cursor.executemany("""
    INSERT OR IGNORE INTO country(country_name)
    VALUES (?)
    """, countries)

    conn.commit()
    conn.close()


def get_countries():
    """Return all cuisines."""

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT country_id, country_name
    FROM country
    ORDER BY country_id
    """)

    countries = cursor.fetchall()

    conn.close()

    return countries


def add_recipe(country_id, name, ingredients):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO recipes(country_id, recipe_name, ingredients)
    VALUES (?, ?, ?)
    """, (country_id, name, ingredients))

    conn.commit()
    conn.close()


def get_recipes(country_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT recipe_id, recipe_name, ingredients
    FROM recipes
    WHERE country_id = ?
    ORDER BY recipe_id
    """, (country_id,))

    recipes = cursor.fetchall()

    conn.close()

    return recipes


def search_recipe(recipe_name):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT recipes.recipe_id,
           recipes.recipe_name,
           recipes.ingredients,
           country.country_name
    FROM recipes
    JOIN country
    ON recipes.country_id = country.country_id
    WHERE recipes.recipe_name LIKE ?
    """, ('%' + recipe_name + '%',))

    recipes = cursor.fetchall()

    conn.close()

    return recipes


def update_recipe(recipe_id, country_id, recipe_name, ingredients):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE recipes
    SET recipe_name=?,
        ingredients=?,
        country_id=?
    WHERE recipe_id=?
    """,
    (recipe_name, ingredients, country_id, recipe_id))

    conn.commit()
    conn.close()


def get_all_recipes():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT recipes.recipe_id,
           recipes.recipe_name,
           recipes.ingredients,
           country.country_name
    FROM recipes
    JOIN country
    ON recipes.country_id = country.country_id
    ORDER BY country.country_id,
             recipes.recipe_id
    """)

    recipes = cursor.fetchall()

    conn.close()

    return recipes

def export_txt():

    recipes = get_all_recipes()

    with open("recipes.txt", "w") as file:

        file.write("====== Recipe List ======\n\n")

        for recipe in recipes:

            file.write(f"Recipe ID   : {recipe[0]}\n")
            file.write(f"Recipe      : {recipe[1]}\n")
            file.write(f"Ingredients : {recipe[2]}\n")
            file.write(f"Cuisine     : {recipe[3]}\n")
            file.write("-" * 35 + "\n")

    print("Recipes exported successfully.")

def delete_recipe(recipe_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM recipes
    WHERE recipe_id = ?
    """, (recipe_id,))

    conn.commit()
    conn.close()

def create_admin():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR IGNORE INTO admin(username, password)
    VALUES(?, ?)
    """, ("admin", "1234"))

    conn.commit()
    conn.close()

def admin_login(password):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM admin
    WHERE username = ?
      AND password = ?
    """, ("admin", password))

    admin = cursor.fetchone()

    conn.close()

    return admin