import json
import requests

recipes_url = "https://apiv2.datadrivencooking.com/v1/community/recipes?pageSize=3000"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjU0OTI5ZjAxLWJmZjYtNGJlZi05ZTkxLWZiMWU0ZjVkYWE2YyIsImVtYWlsIjoiZGVtb0B1bm94LmNvbSJ9.NLn5iiIrh0jE9hz5YpPAKrnWF1-_QjyH90DMVi6mZ24"
}
response = requests.get(recipes_url, headers=headers)

if response.status_code == 200:
    with open("data/community_recipes.json", "w") as file:
        json.dump(response.json(), file, indent=4)
