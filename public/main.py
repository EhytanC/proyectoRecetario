from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from lookfor import Look_for_ingredients, Look_recipes_byName, Look_recipes_byId
number_of_ingredients = [1]
app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="templates")

class Recipe(BaseModel):
    id:int
    name:str
    description:str
    ingredients:list

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

@app.post('/add_ingredient')
def add_ingredient():
    number_of_ingredients.append(number_of_ingredients[-1] + 1)
    return RedirectResponse('/recetas',303)
