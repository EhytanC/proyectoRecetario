import pandas as pd
df_itr = pd.read_csv('../db/ingredients_recipes.csv')
df_ingredients = pd.read_csv('../db/ingredients.csv')
df_recipes = pd.read_csv('../db/recipes.csv')

def Look_recipes_byName(search:str):
    df_recipes = pd.read_csv('../db/recipes.csv')
    
    search = search.lower()
    df = df_recipes[df_recipes['name'].str.contains(search)]
    df = df.to_dict('records')
    return df


def Look_for_ingredients(id_recipes):
    df_itr = pd.read_csv('../db/ingredients_recipes.csv')
    df_ingredients = pd.read_csv('../db/ingredients.csv')
    
    id_ingredients = []
    name_ingredients = []

    for i in id_recipes:
        id_ingredients.append(df_itr['ingredient_id'][df_itr['recipe_id'] == i].tolist())
    for i in id_ingredients:
        name_ingredients.append(df_ingredients['name'][df_ingredients['id'].isin(i)].to_list())
    # elif type(id_recipes) == int:
    #     name_ingredients = df_ingredients['name'][df_ingredients['id'].isin(i)].to_list()
    return name_ingredients

def Look_recipes_byId(id_recipes:int):
    df_recipes = pd.read_csv('../db/recipes.csv')

    recipe = df_recipes[df_recipes['id'] == id_recipes]
    return recipe.to_dict('records')

def Look_forId_ingredients(name_ingredient:str):
    df_ingredients = pd.read_csv('../db/ingredients.csv')
    
    name_ingredient = name_ingredient.lower()
    index_ingredient = df_ingredients[df_ingredients['name'] == name_ingredient].index
    if index_ingredient.empty:
        return 0
    id_ingredient = df_ingredients.loc[index_ingredient[0]][0]
    return id_ingredient