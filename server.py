from flask import Flask, url_for, request, redirect, abort, jsonify
from surfboardDao import surfboardDao


app = Flask(__name__, static_url_path='', static_folder='staticpages')

#Create array as object


@app.route('/')
def index():
    return  "Hello, Megh. I made a website. Its online. Its just this line, but i think its cool."


# curl http://127.0.0.1:5000/surfboards
# Get all boards
@app.route('/surfboards')
def getAll():
    return jsonify(surfboardDao.getAll())


#Find by id
@app.route('/surfboards/<int:ID>')
def findById(ID):
    
    return jsonify(surfboardDao.findById(ID)) 
    

#Create

#Test
# curl -X POST -H "content-type:application/json" -d "{\"ID\":1,\"make\":\"test\",\"model\":\"someboard\",\"type\":\"longboard\",\"price\":123000}" http://127.0.0.1:5000/surfboards

@app.route('/surfboards', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)

    surfboard = {
        "ID": request.json["ID"], 
        "make": request.json["make"], 
        "model": request.json["model"], 
        "type": request.json["type"], 
        "price": request.json["price"]
    }
    
    return jsonify(surfboardDao.create(surfboard))
    return "served by create"

#Update

# curl -X POST -H "content-type:application/json" -d "{\"ID\":1,\"make\":\"test\",\"model\":\"someboard\",\"type\":\"longboard\",\"price\":123000}" http://127.0.0.1:5000/surfboards
#  curl -X PUT -H "content-type:application/json" -d "{\"make\":\"Myboards\",\"model\":\"bestboard\",\"type\":\"Fish\",\"price\":9999999}" http://127.0.0.1:5000/surfboards/1

@app.route('/surfboards/<int:ID>', methods=['PUT'])
def update(ID):
    foundSurfboard = surfboardDao.findById(ID) #list(filter(lambda t : t["id"]== id, surfboards))
    print(foundSurfboard)
    if foundSurfboard == {}:
        return jsonify({}), 404
    currentSurfboard = foundSurfboard
    if 'make' in request.json:
        currentSurfboard['make'] = request.json['make']
    if 'model' in request.json:
        currentSurfboard['model'] = request.json['model']
    if 'type' in request.json:
        currentSurfboard['type'] = request.json['type']
    if 'price' in request.json:
        currentSurfboard['price'] = request.json['price']
    surfboardDao.update(currentSurfboard)
    return jsonify(currentSurfboard)

#Delete
# curl -X DELETE http://127.0.0.1:5000/surfboards/4
@app.route('/surfboards/<int:ID>', methods=['DELETE'])
def delete(ID):
    deleteSurfboard = surfboardDao.delete(ID) 
    if deleteSurfboard == {}:
        print("Surfboard does not exist")
        return jsonify({}), 404
        
        
    surfboardDao.delete(ID)

    return jsonify({"Done":True})

if __name__ == "__main__":
    print("in if")
    app.run(debug=True)