import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

recipeResponce = requests.get('https://eda.ru/recepty/vypechka-deserty/hvorost-91376', headers={'User-Agent': UserAgent().firefox})
soupRecipe = BeautifulSoup(recipeResponce.text, 'html.parser')

ingredientsTag = soupRecipe.find_all(itemprop='recipeIngredient')
ingredients =[]
for i in ingredientsTag:
    ingredients.append(i.get_text().replace('\r\n', '').replace('  ', ''))

print(ingredients)

urlSearch = 'https://www.vprok.ru/catalog/search?text={ingredient}'
ingredientsResponse = requests.get(urlSearch.format(ingredient=ingredients[0]), headers={'User-Agent': UserAgent().firefox})
soupIngredients = BeautifulSoup(ingredientsResponse.text, 'html.parser')

print(soupIngredients.h1)