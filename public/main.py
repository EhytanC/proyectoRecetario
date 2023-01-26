from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from lookfor import Look_for_ingredients, Look_recipes_byName, Look_recipes_byId

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="templates")

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