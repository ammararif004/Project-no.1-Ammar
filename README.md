# Project-no.1-Ammar

# App Link: https://project-no1-ammar-skgjfbpperc4zbsccmunto.streamlit.app/

# Video Link: https://1drv.ms/v/c/a29fad3f22dc046a/IQATfWTBjSCbQqsjeNC0oihxAREiHqm4ovuUu1V7w76I7Rg?e=krIhBA

# Project Description

Digital Cookbook is a recipe manager web app built with Python, Streamlit and pandas. It lets home cooks store, search and manage their favorite meals and ingredients. Recipes are saved in a CSV file and held in st.session_state during the session, so every page uses the same up-to-date data.

Work Completed

Phase 1: Core requirements

Navigation menu to switch between Home, Search, Add Recipe, View All and Surprise Me.
Add Recipe: a form with recipe name, comma-separated ingredients, preparation time, instructions and difficulty level (Easy, Medium, Hard). New recipes are saved to the CSV file.
Search: type one or more ingredients separated by commas, and the app shows every recipe that contains all of them, with the ingredients and instructions in expandable boxes.
View All: shows all saved recipes in a table, with each recipe’s instructions below.
Surprise Me: a button that displays a randomly selected recipe.
Data storage: a CSV file for storage, and st.session_state to hold recipe data during the session.

Phase 2: Advanced requirements

Categories: each recipe is tagged Breakfast, Lunch, Dinner, Dessert or Healthy using a dropdown.
Ratings and sorting: users rate recipes from 1 to 5 stars, and the View All table sorts by rating (highest first).
Servings scaler: users enter the number of servings they want, and the ingredient quantities scale automatically.

Phase 3: Student’s choice innovation

Cooking video instructions: each recipe can store a video link when it is added. The video plays inside the app on the View All page, so users can watch how to make the recipe.

