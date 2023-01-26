import pandas as pd
df_itr = pd.read_csv('../db/ingredients_recipes.csv')
df_ingredients = pd.read_csv('../db/ingredients.csv')
df_recipes = pd.read_csv('../db/recipes.csv')

def Record_recipe(recipe_to_post, id_ingredients):
    df = pd.DataFrame(recipe_to_post)
    df = pd.concat([df,df_recipes])
    print('\n'*2,df.head(5),'\n'*2)
    return 0