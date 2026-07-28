#----------------------------------
# RECIPE MANAGEMENT SYSTEM
# Group Project
# Main program the main function
#----------------------------------

import database
from person import User, Admin
database.create_table()
database.country_cuisine()
database.create_admin()

#-----------------------------------
# Display menu (Before Login)
def main_menu():
     
    print("\n==========================================")
    print(" RECIPE MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Login")
    print("0. Exit")
    print("==========================================")

#----------------------------------
# Display login_menu
def login_menu():

    print("\n=============== LOGIN ==================")
    print("1. User")
    print("2. Admin")
    print("0. Back")

#----------------------------------
# Display user menu (After Login)
def user_menu(username):

    print("\n==================================================")
    print("        RECIPE MANAGEMENT SYSTEM")
    print("==================================================")
    print(f"Logged in as: {username}\n")
    print("1. Browse by Country")
    print("2. Search Recipe")
    print("3. Export Recipes")
    print("4. Logout")
    print("0. Exit")

#----------------------------------
# Display user menu (After Login)
def admin_menu(admin):

    print("\n==================================================")
    print("        RECIPE MANAGEMENT SYSTEM")
    print("==================================================")
    print(f"Logged in as: {admin}\n")
    print("1. Browse by Country")
    print("2. Search Recipe")
    print("3. Add Recipe")
    print("4. Update Recipe")
    print("5. Delete Recipe")
    print("6. Export Recipes")
    print("7. Logout ")
    print("0. Exit")

#----------------------------------
# Main program to run
while True:

        main_menu()
        choice = input("Choose: ")

        #-----------------
        # ==== Login into program ====
        if choice == "1":

            #==== start menu while loop ====
            while True:

                login_menu()
                login = input("Login as: ")

                #-------------------------
                #==== User Login ====
                if login == "1":

                    #username = object for temporary user
                    user = User("User")
                    print(user)
                    while True:

                        #retrieve from person.py
                        user_menu(user.get_username())

                        #==== User: Browse by country  ====
                        option = input("Choose an option: ")
                        if option == "1":

                            print("\nBrowse by Country")
                            countries = database.get_countries()

                            for country in countries:
                                print(f"{country[0]}. {country[1]}")

                            country_id = input("\nEnter cuisine number: ")
                            recipes = database.get_recipes(country_id)

                            if not recipes:
                                print("No recipes found.")

                            else:
                                print()

                            for recipe in recipes:
                                print(f"ID: {recipe[0]}")
                                print(f"Name: {recipe[1]}")
                                print(f"Ingredients: {recipe[2]}")
                                print("-" * 30)

                        #==== User: Search recipe by names ====                        
                        elif option == "2":
                            search = input("\nEnter recipe name: ")
                            
                            recipes = database.search_recipe(search)

                            if not recipes:
                                print("\nRecipe not found.")

                            else:
                                print("\nSearch Results: ")

                                for recipe in recipes:
                                    print("----------------------")
                                    print("ID:", recipe[0])
                                    print("Recipe:", recipe[1])
                                    print("Ingredients:", recipe[2])
                                    print("Cuisine:", recipe[3])

                        #==== User: Export ====
                        elif option == "3":

                            database.export_txt()
                            print("Recipes exported to recipe.txt")

                        elif option == "4":
                            break

                        elif option == "0":
                            print("\nExit Successful.")
                            print("Thank you for using Smart Recipe Management System.")
                            exit()

                        else:
                            print("\nInvalid choice. Please try again.")

                #--------------
                #==== Admin login ====
                elif login == "2":

                    password = input("Enter Admin Password: ")
                    admin_data = database.admin_login(password)

                    if admin_data:
                        print("\nLogin Succesful!")

                        #==== polymorphism example ====
                        admin = Admin("Admin") 
                        print(admin)

                        while True:

                            admin_menu(admin.get_username())
                            option = input("Choose an option: ")

                            #==== Admin: Browse by country ====
                            if option == "1":
                                print("\nBrowse by Country")

                                countries = database.get_countries()

                                for country in countries:
                                    print(f"{country[0]}. {country[1]}")

                                #==== Using country id ====
                                country_id = input("\nEnter cuisine number: ")
                                recipes = database.get_recipes(country_id)

                                if not recipes:
                                    print("No recipes found.")

                                else:
                                    print()

                                for recipe in recipes:
                                    print(f"ID: {recipe[0]}")
                                    print(f"Name: {recipe[1]}")
                                    print(f"Ingredients: {recipe[2]}")
                                    print("-" * 30)

                            #==== Search recipe by names ====
                            elif option == "2":
                                search = input("\nEnter recipe name: ")

                                recipes = database.search_recipe(search)

                                if not recipes:
                                    print("\nRecipe not found.")

                                else:
                                    print("\nSearch Results: ")

                                    for recipe in recipes:
                                        print("----------------------")
                                        print("ID:", recipe[0])
                                        print("Recipe:", recipe[1])
                                        print("Ingredients:", recipe[2])
                                        print("Cuisine:", recipe[3])

                            #==== Add recipe into database ====
                            elif option == "3":

                                countries = database.get_countries()
                                print("\n========== Add Recipe ==========")

                                for country in countries:
                                    print(f"{country[0]}. {country[1]}")
                                
                                print("0. Back")

                                #==== Use country id ====
                                country_choice = input("\nChoose: ")

                                #==== return to page before update menu ====
                                if country_choice == "0":
                                    continue

                                recipe_name = input("Recipe Name: ")
                                ingredients = input("Ingredients: ")

                                database.add_recipe(
                                    country_choice,
                                    recipe_name,
                                    ingredients
                                )

                                print("\nRecipe added successfully!")

                            #==== Update recipe in database ====
                            elif option == "4":
                                    
                                print("\n===== Update Recipe =====")
                                recipe_id = input("Enter recipe ID to update: ")

                                print("Choose new cuisine: ")
                                countries = database.get_countries()

                                for country in countries:
                                    print(f"{country[0]}. {country[1]}")

                                print("0. Back")

                                country_id = input("Enter new cuisine ID: ")

                                #==== return from update menu ====
                                if country_id == "0":
                                    continue

                                name = input("Enter new recipe name: ")
                                ingredients = input(
                                    "Enter new ingredients (separated by comma): ")

                                database.update_recipe(
                                    recipe_id,
                                    country_id,
                                    name,
                                    ingredients
                                )

                                print("\nRecipe updated successfully!")
                                
                            #==== Delete recipe from database ====
                            # Please export file first to know recipe ID before deletion
                            elif option == "5":

                                recipe_id = input("Enter recipe ID to delete: ")
                                confirm = input("Are you sure you want to delete? (y/n): ")

                                if confirm.lower() == "y":

                                    database.delete_recipe(recipe_id)
                                    print("Recipe deleted successfully!")

                                else:
                                    print("Delete cancelled")

                            #==== Export current database into text file ====
                            elif option == "6":

                                database.export_txt()
                                print("Recipes exported to recipe.txt")

                            #-----------------------
                            #==== Logout and back to login menu ====   

                            elif option == "7":
                                break

                            
                            elif option == "0":
                                print("\nExit Successful.")
                                print("Thank you for using Smart Recipe Management System.")
                                exit()

                            else:
                                print("\nInvalid login option.")

                    else:
                        print("\nInvalid password")

                elif login == "0":
                    break

        #==== Exit the program ====
        elif choice == "0":

            print("\nThank you for using Smart Recipe Management System.")
            break

        else:

            print("\nInvalid menu choice. Please try again.")
                            