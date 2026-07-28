# To demostrate inheritance and meet the OOP requirement

class Person:
    def __init__(self, username):
        self._username = username

    def get_username(self):
        return self._username

    def __str__(self):
        return self._username
    


class User(Person):
    def __init__(self, username):
        super().__init__(username)

    def browse_by_country(self):
        print("\nBrowse by Country")

    def search_recipe(self):
        print("\nSearch Recipe")

    def export_recipes(self):
        print("\nExport Recipes")


class Admin(User):      # <-- inherits from User
    def __init__(self, username):
        super().__init__(username)

    # polymorphism 
    def __str__(self):
        return f"Administrator: {self._username}"

    def add_recipe(self):
        print("\nAdd Recipe")

    def update_recipe(self):
        print("\nUpdate Recipe")

    def delete_recipe(self):
        print("\nDelete Recipe")