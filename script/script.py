import json
import csv

with open("users.json", "r") as f_users:
    users = json.load(f_users)

user_result = [
    {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }
    for user in users
    if all(user.get(k) for k in ("name", "gender", "address", "age"))
]

books = []
with open("books.csv", "r") as f_books:
    reader = csv.DictReader(f_books)
    for row in reader:
        books.append({
            "title": row["Title"],
            "author": row["Author"],
            "pages": int(row["Pages"]),
            "genre": row["Genre"]
        })

for i, book in enumerate(books):
    user_index = i % len(user_result)
    user_result[user_index]["books"].append(book)

with open("result.json", "w") as f_res:
    json.dump(user_result, f_res, ensure_ascii=False, indent=4)



