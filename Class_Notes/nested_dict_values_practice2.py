# working with nested lists of dictionaries

clothes_list = [{
    "ID": "1000201",
    "Name": "Clothes Name",
    "Price": 24.1,
    "Category": "Trousers",
    "Reviews": [{
        "User": "username1200", "Review": "some review", "Score": 2
    }, {'User': 'username341', 'Review': 'Some review 2', 'Score': 4},
        {'User': 'username34841', 'Review': 'Some review 3', 'Score': 2},{
        "User": "username1200", "Review": "some review 4 by same user", "Score": 2
    },]
}]

#### expanded
def get_reviews(username):
    a = []
    for i in range(len(clothes_list)):
        for x in clothes_list[i]["Reviews"]:
            if x["User"] == username:
                a.append(x)
    return a


print(get_reviews("username1200"))


#### simplified
# username = "username1200"
# print([review for clothes_item in clothes_list for review in clothes_item["Reviews"] if review["User"] == username])
