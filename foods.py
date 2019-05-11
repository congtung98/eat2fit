from pymongo import MongoClient

mongo_uri = "mongodb+srv://admin:admin@cluster0-bvpux.mongodb.net/test?retryWrites=true"

client = MongoClient(mongo_uri)

food_app = client.db_food

Foods = food_app['foods']

while True:
    title = input('Mời bạn nhập tên thức ăn: ')
    price = int(input('Mời bạn nhập giá đồ ăn: '))
    resources = input('Mời bạn nhập thành phần: ')
    calories = int(input('Mời bạn nhập tổng lượng calo: '))
    protein = float(input('Mời bạn nhập lượng protein: '))
    carb = float(input('Mời bạn nhập lượng carb: '))
    fat = float(input('Mời bạn nhập lượng fat: '))

    food_document = {
        "title" : title,
        "price" : price,
        "resources" : resources,
        "calories" : calories,
        "protein" : protein,
        "carb" : carb,
        "fat" : fat,
    }

    Foods.insert_one(food_document)