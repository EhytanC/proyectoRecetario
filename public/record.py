import pandas as pd
df_itr = pd.read_csv('../db/ingredients_recipes.csv')
df_ingredients = pd.read_csv('../db/ingredients.csv')
df_recipes = pd.read_csv('../db/recipes.csv')

def Record_recipe(recipe_to_post, id_ingredients):
    data = []
    for i in id_ingredients:
        data.append({'recipe_id':int(recipe_to_post['id'][-1]),'ingredient_id':i})
    ingredients_post = pd.DataFrame(data)
    df_ingredients_post = pd.concat([ingredients_post,df_itr])

    df_recipes_post = pd.DataFrame(recipe_to_post)
    df_recipes_post = pd.concat([df_recipes_post,df_recipes])
    
    df_ingredients_post.to_csv('../db/ingredients_recipes.csv', index=False)
    df_recipes_post.to_csv('../db/recipes.csv', index=False)

    print(df_recipes_post.head(3),'\n'*3, df_ingredients_post.head(20))