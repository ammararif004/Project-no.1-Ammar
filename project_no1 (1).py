import streamlit as st
import pandas as pd

def scale_line(line, factor):           #servings scaling function
    parts = line.strip().split(" ", 1)
    try:
        number = float(parts[0]) * factor
    except ValueError:
        return line.strip()
    rest = parts[1] if len(parts) > 1 else ""
    return f"{number:g} {rest}"

if "df" not in st.session_state:               
    st.session_state.df = pd.read_csv("recipes.csv").reindex(columns=["Recipe","Category","Ingredients","Servings","Estimated time","Instructions","Difficulty level","Rating","Video"])
    if "Servings" not in st.session_state.df.columns:
        st.session_state.df["Servings"] = 1
if "Video" not in st.session_state.df.columns:
        st.session_state.df["Video"] = ""
        
with st.sidebar:
    page_chosen=st.pills("Navigation Panel", ("Home", "Search", "Add Recipe", "View All", "Surprise Me"))

if page_chosen == "Home":                      # Home Page
    st.title("Welcome to Your Digital Cookbook")

if page_chosen == "Search":
    st.title("Search for a recipe")
    Ingredient = st.text_input("Type Ingredient:", "")
    original_df = pd.read_csv("recipes.csv")
    wanted = [item.strip().lower()
              for item in Ingredient.split(",")
              if item.strip()]
    if wanted:
        def matches(ingredients):         # matching ingredients function
            return all(item in ingredients.lower() for item in wanted)
        results = original_df[
            original_df["Ingredients"].fillna("").apply(matches)
        ]

        if results.empty:
            st.warning("No matching recipes found.")
        else:
            for _, r in results.iterrows():
                with st.expander(r["Recipe"]):
                    st.write(f"**Difficulty:** {r['Difficulty level']}  |  **Time:** {r['Estimated time']} min")
                    st.write("**Ingredients:**")
                    for item in str(r["Ingredients"]).split(","):
                        st.write("- " + item.strip())
                    st.write("**Instructions:**")
                    st.text(r["Instructions"])
    else:
        st.dataframe(original_df, hide_index=True)

if page_chosen == "Add Recipe":
    st.title("Add a new Recipe!")
    Name = st.text_input("Recipe name", "")
    Category = st.multiselect("Category",["Breakfast", "Lunch", "Dinner", "Dessert","Healthy"])
    Ing=st.text_area("Ingredients (comma separated)", placeholder="200 g pasta, 3 cloves, 1 garlic, 2 tbsp olive oil",)
    Servings = st.number_input("Servings this recipe makes", min_value=1, value=1, step=1)
    Prep=st.number_input("Estimated preparation time in minutes",step=1)
    Ins=st.text_area("Instructions","")
    Video = st.text_input("Cooking video link (optional)", "")
    diff=st.selectbox("Difficulty level",("Easy","Medium","Hard"))
    if st.button("Add Recipe"):
        st.success("Recipe Saved!")
        recipe_df = pd.DataFrame({"Recipe": [Name],"Category":[", ".join(Category)], "Ingredients": [Ing], "Servings":[Servings], "Estimated time": [Prep],"Instructions":[Ins],"Difficulty level":[diff],"Rating": [float("nan")], "Video": [Video.strip()]})

        original_df = pd.read_csv("recipes.csv")
        st.session_state.df = pd.concat([original_df, recipe_df], ignore_index=True)
        st.session_state.df.to_csv('recipes.csv', index=False)
        
        
if page_chosen=="View All":
    st.title("All Saved Recipes")
    df=st.session_state.df  
    sorted_df = df.sort_values(by="Rating",ascending=False,na_position="last")
    st.dataframe(sorted_df, hide_index=True)  

    df = st.session_state.df
    recipe_name = st.selectbox("Choose recipe", df["Recipe"])
    row = df[df["Recipe"] == recipe_name].iloc[0]
    st.subheader("Instructions")
    st.text(row["Instructions"])
    st.subheader("Scale ingredients")
    base = int(row["Servings"]) if pd.notna(row["Servings"]) else 1
    servings_wanted = st.number_input("Servings wanted", min_value=1, value=base, step=1)
    factor = servings_wanted / base
    for item in str(row["Ingredients"]).split(","):
        st.write("- " + scale_line(item, factor).strip())

        
    st.subheader("Cooking video")
    video = row.get("Video", "")
    video = "" if pd.isna(video) else str(video).strip()
    if video:
        st.video(video)
    else:
        st.info("No video added for this recipe.")

    st.write("Rate this recipe")
    stars = st.feedback("stars", key=f"rate_{recipe_name}")
    if stars is not None and df.loc[df["Recipe"] == recipe_name, "Rating"].iloc[0] != stars + 1:
        df.loc[df["Recipe"] == recipe_name, "Rating"] = stars + 1
        df.to_csv("recipes.csv", index=False)
        st.rerun()
        
if page_chosen=="Surprise Me":
    st.title("Random Recipe")

    original_df = pd.read_csv("recipes.csv")

    if st.button("Pick a random recipe"):
        surprise = original_df.sample(n=1)
        st.dataframe(surprise, hide_index=True)
