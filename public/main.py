from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from lookfor import Look_for_ingredients, Look_recipes_byName, Look_recipes_byId, Look_forId_ingredients
from record import Record_recipe
app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")

templates = Jinja2Templates(directory="templates")
number_of_ingredients = [1]

@app.get('/buscador')
def seeker(request: Request, search:str|None = None):
    data_result = []

    if type(search) == str:
        data_result = Look_recipes_byName(search)
        id_recipes = []
        for i in data_result:
            id_recipes.append(i['id'])
        names_ingredients = Look_for_ingredients(id_recipes)
        i=0
        for recipes in data_result:
            recipes['ingredients'] = names_ingredients[i]
            i += 1

    return templates.TemplateResponse('search.html', {'request': request, 'data':data_result})

@app.get('/recetas/{id_recipe}')
def look_recipe(request:Request, id_recipe:int):
    data = Look_recipes_byId(id_recipe)
    data[-1]['ingredients'] = Look_for_ingredients([data[-1]['id']])[-1]
    return templates.TemplateResponse('look_recipe.html',{'request': request, 'data':data})

@app.get('/recetas')
def post_recipe(request:Request):
    return templates.TemplateResponse('post_recipe.html', {'request':request, 'number_of_ingredients':number_of_ingredients})

@app.post('/recetas')
async def post_recipe(request:Request):
    form_data = await request.form()
    id_ingredients = []
    recipe_to_post = {
        'id': [form_data['id_recipe']],
        'name': [form_data['name_recipe']],
        'description': [form_data['description']],
        }
    for i in number_of_ingredients:
        id_ingredients.append(Look_forId_ingredients(form_data[f'ingredient{i}']))
    print(f'{id_ingredients}\n{recipe_to_post}\n')
    Record_recipe(recipe_to_post,id_ingredients)
    return RedirectResponse('/recetas', 303)

@app.get('/add_ingredient')
def add_ingredient(delete:bool = False):
  
    if len(number_of_ingredients) == 1 and delete:
        return RedirectResponse('/recetas',303)

    if delete:
        number_of_ingredients.pop()
        return RedirectResponse('/recetas',303)
  
    number_of_ingredients.append(number_of_ingredients[-1] + 1)
    return RedirectResponse('/recetas',303)