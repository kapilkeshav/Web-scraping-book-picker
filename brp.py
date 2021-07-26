import pymongo
import random
conn = pymongo.MongoClient(
    'localhost',
    27017    
)
db = conn['brp']
collections = db['brp_tb']
all = collections.find()
u = random.randint(0,50)
x = random.randint(0,u)
y = ''

for i in range(x):
    y=all[i]
print("The book that you should read is: " + y['book'])
