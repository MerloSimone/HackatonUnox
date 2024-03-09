import json
import requests


headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjU0OTI5ZjAxLWJmZjYtNGJlZi05ZTkxLWZiMWU0ZjVkYWE2YyIsImVtYWlsIjoiZGVtb0B1bm94LmNvbSJ9.NLn5iiIrh0jE9hz5YpPAKrnWF1-_QjyH90DMVi6mZ24"
}

recipes = {}
with open("data/community_recipes.json", "r") as file:
    recipes = json.load(file)

for recipe in recipes:
    title = recipe["title"]
    recipe_id = recipe["id"]

    response = requests.get(f"https://apiv2.datadrivencooking.com/v1/company/recipes/{recipe_id}", headers=headers)

    if response.status_code == 200:
        with open(f"data/recipe/{recipe_id}-{title}.json", "w") as file:
            json.dump(response.json(), file, indent=4)
