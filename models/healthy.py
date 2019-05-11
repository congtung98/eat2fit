from pymongo import MongoClient
from bson.objectid import ObjectId


mongo_uri = 'mongodb+srv://admin:admin@cluster0-aekow.mongodb.net/test?retryWrites=true'
client = MongoClient(mongo_uri)

db = client.database

Myfood = db['my_food']

# food_document = [
#     {
#     'image':'ga.jpg',
#     'title':'Cơm gạo lứt, thịt gà sốt Leekumki',
#     'price':'70000',
#     'resources':'150gr cơm gạo lứt, 150gr thịt ức gà, 200gr rau củ ',
#     'calo':'388',
#     'carb':'44,4',
#     'protein':'36,4',
#     'fat':'6,2'
#     },
#     {
#     'image':'thitlon.jpg',
#     'title':'Cơm gạo lứt, thịt heo sốt Teriyaki',
#     'price':'70000',
#     'resources':'150gr cơm gạo lứt, 150gr thịt heo, 200gr rau củ',
#     'calo':'374',
#     'carb':'44,4',
#     'protein':'36,4',
#     'fat':'4,7'
#     },
#     {
#     'image':'trung.jpg',
#     'title':'Cơm gạo lứt, trứng thịt băm cốt dừa',
#     'price':'50000',
#     'resources':'150gr cơm gạo lứt, 200gr trứng thịt băm,200gr rau củ',
#     'calo':'525',
#     'carb':'50,3',
#     'protein':'24,7',
#     'fat':'22,6'
#     },
#     {
#     'image':'ca.jpg',
#     'title':'Cơm gạo lứt, cá phi lê hấp tương gừng',
#     'price':'60000',
#     'resources':'150gr cơm gạo lứt, 200gr cá, 200gr rau củ',
#     'calo':'410',
#     'carb':'44,4',
#     'protein':'44,3',
#     'fat':'6,3'
#     },
#     {
#     'image':'thitvien.jpg',
#     'title':'Cơm gạo lứt, thịt thăn heo viên hấp',
#     'price':'60000',
#     'resources':'150gr cơm gạo lứt , 200gr thịt băm viên,200gr rau củ ',
#     'calo':'488',
#     'carb':'44,4',
#     'protein':'43,9',
#     'fat':'15,7'
#     },
#     {
#     'image':'bo.jpg',
#     'title':'Cơm gạo lứt, thịt bò kho vang đỏ',
#     'price':'70000',
#     'resources':'-	150gr cơm gạo lứt, 150gr thịt bò, 200gr rau củ',
#     'calo':'429',
#     'carb':'44,4',
#     'protein':'55,9',
#     'fat':'10,7'
#     },
#     {
#     'image':'combo.jpg',
#     'title':'Cơm trắng, thịt bò xào',
#     'price':'50000',
#     'resources':'300gr cơm trắng,150gr thịt bò ,100gr dưa chuột',
#     'calo':'707',
#     'carb':'90',
#     'protein':'58',
#     'fat':'9,6'
#     },
#     {
#     'image':'comga.jpg',
#     'title':'Cơm trắng, thịt gà sốt Leekumki',
#     'price':'50000',
#     'resources':'300gr cơm trắng, 200gr thịt gà , 250gr súp lơ',
#     'calo':'690',
#     'carb':'88,2',
#     'protein':'52,8',
#     'fat':'7,3'
#     },
#     {
#     'image':'tom.jpg',
#     'title':'Cơm trắng, tôm hấp',
#     'price':'60000',
#     'resources':'300gr cơm trắng,200gr tôm, 150gr rau',
#     'calo':'615',
#     'carb':'91',
#     'protein':'51,7',
#     'fat':'2,8'
#     },
#     {
#     'image':'comga2.jpg',
#     'title':'Cơm trắng, thịt gà rang',
#     'price':'60000',
#     'resources':'300gr cơm trắng,200gr thịt gà,150gr đỗ xào',
#     'calo':'655',
#     'carb':'91',
#     'protein':'51,9',
#     'fat':'6,6'
#     }
# ]

# Myfood.insert_many(food_document)

