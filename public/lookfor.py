import pandas as pd
df_itr = pd.read_csv('../db/ingredients_recipes.csv')
df_ingredients = pd.read_csv('../db/ingredients.csv')
df_recipes = pd.read_csv('../db/recipes.csv')

def Look_recipes_byName(search:str):
    search = search.lower()
    df = df_recipes[df_recipes['name'].str.contains(search)].tail(20)
    df = df.to_dict('records')
    return df


def Look_for_ingredients(id_recipes):
    
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
    recipe = df_recipes[df_recipes['id'] == id_recipes]
    return recipe.to_dict('records')

def Look_forId_ingredients(name_ingredient:str):
    name_ingredient = name_ingredient.lower()
    df = df_ingredients[df_ingredients['name'] == name_ingredient]
    if df.empty:
        return 0
    print(df,'\n'*4)
    id_ingredient = df.loc[0][0]
    return id_ingredient
    
# def Look_for_ingredient(id_recipe:int, name = False):
#     id_ingredients = df_itr[df_itr["recipe_id"] == id_recipe].ingredient_id.values
#     if name:
#         name_ingredients = df_ingredients.loc[id_ingredients].name.values
#         return name_ingredients
#     return id_ingredients

# def ingredientes_receta(id_receta, id_ingredientes):
#     df_res = pd.DataFrame()
#     print(id_receta, id_ingredientes)
#     for i in range(len(id_ingredientes)):
#         df = pd.DataFrame(data={'ingredient_id':[id_ingredientes[i]], 'recipe_id':[id_receta]})
#         df_res = pd.concat([df, df_res])
#     print(df_res)
#     df_res = pd.concat([df_itr,df_res])
#     df_res.to_csv('../db/ingredients_recipes_test.csv', index=False)