
# définition de la fonction qui trouvera une recette en fonction d'ingrédients fournis
# la fonction ne prend pour l'instant qu'un seul argument
# import des bibliothèques requises
import os
import openai
import csv

# données d'identification et d'authentification openAI
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG")

# le moteur IA utilisé dans ce programme
engine = "text-davinci-002"

# la liste suivante est ici hardcodée mais sera générée depuis une liste d'ingrédients suggérés par l'interface utilisateur (frontend)
ingredients_from_UI = ["beef","ginger","bell peppers","oregano"]

# à partir de la liste d'ingrédients, génération d'une chaîne de caractères qui s'intègrera naturellement dans la question posée
formatted_ingredients = "\n- " + "\n- ".join(ingredients_from_UI)

# la question qui sera posée au modèle openAI
question_asked_to_openAI_completions = "Provide a cooking recipe based on the following ingredients:\n" + formatted_ingredients + "\n\nThe response should include the recipe's name, the recipe's ingredients, and the recipe's instructions."

# un dictionnaire contenant les arguments à passer à l'endpoint "completions" via la méthode "openai.Completion.create" (SDK openAI)
completion_arguments = {
  "engine" : engine,
  "prompt" : question_asked_to_openAI_completions,
  "temperature" : 0.7,
  "top_p" : 1,
  "max_tokens" : 300,
  "frequency_penalty" : 0,
  "presence_penalty" : 0
  }

def findrecipe(ingredients):
    response = openai.Completion.create(
        engine = completion_arguments["engine"],
        prompt =  completion_arguments["prompt"],
        temperature = completion_arguments["temperature"],
        top_p = completion_arguments["top_p"],
        max_tokens = completion_arguments["max_tokens"],
        frequency_penalty = completion_arguments["frequency_penalty"],
        presence_penalty = completion_arguments["presence_penalty"])

    complete_recipe = response["choices"][0]["text"][2:]

    recipe_name = complete_recipe[:complete_recipe.find("\n")-1]

    ingredients_extraction = complete_recipe[complete_recipe.find("Ingredients:") + 14 : complete_recipe.find("Instructions:")-2]
    instructions_extraction = complete_recipe[complete_recipe.find("Instructions:") + 15:]

    ingredients_list = list(ingredients_extraction.split('\n'))
    ingredients_list = list(i.strip('- ') for i in ingredients_list)
    ingredients_list = list(filter(lambda a: a != '', ingredients_list))

    instructions_list = list(instructions_extraction.split('\n'))
    instructions_list = list(i[3:] for i in instructions_list)
    instructions_list = list(filter(lambda a: a != '', instructions_list))

    print("=========================================\n"+str(response)+"\n=========================================\n")

    result = {
        "RecipeName" : recipe_name,
        "Ingredients" : ingredients_list,
        "Instructions" : instructions_list
    }

    print(result)

    return result

def csv_to_dict(csv_file):
    fields = []
    rows = []
    result = dict()
    with open(csv_file, 'r') as infile:
        csvreader = csv.reader(infile,delimiter=',')
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    for category in range(len(fields)):
        if category%2 == 0:
            to_insert = []
            print(len(rows[category]))
            for ingredient in range(len(rows)):
                print(fields[category])
                print(to_insert)
                if rows[ingredient][category] != '':
                    to_insert.append(rows[ingredient][category])
            result[fields[category]] = to_insert
    return result

print(csv_to_dict("what_to_cook/api_home/ingredients_list.csv"))