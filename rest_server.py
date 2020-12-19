from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#Create array as object

surfboards = [ 
    {"id":1, "Make":"Lost", "Model":"DRIVER 2.0: 5'2 ", "Type":"Shortboard", "Price":75000},
    {"id":2, "Make":"Lost", "Model":"Hydra: 5'0", "Type":"Fish", "Price":80000},
    {"id":3, "Make":"Firewire", "Model":"The Gem: 10'0", "Type":"Longboard", "Price":100000},
    {"id":4, "Make":"Pyzel", "Model":"Shadow: 5'10", "Type":"Shortboard", "Price":71500}
]
nextId=5



@app.route('/')
def index():
   return  "Hello, Megh. I made a website. Its online. Its just this line, but i think its cool."

# Get all boards
@app.route('/surfboards')
def getAll():
    return jsonify(surfboards)


#Find by id
@app.route('/surfboards/<int:id>')
def findById(id):
    foundSurfboard = list(filter(lambda t : t["id"]== id, surfboards))
    if len(foundSurfboard) == 0:
        return jsonify({}), 204
    return jsonify(foundSurfboard[0]) #returns first book if more than one book with same id
    #print(foundSurfboard) #for testing
    return "served by findById with id = "+str(id)

#Create


# curl -X POST -H "content-type:application/json" -d "{\"Make\":\"test\",\"Model\":\"someboard\",\"Type\":\"Longboard\",\"Price\":123000}" http://127.0.0.1:5000/surfboards

@app.route('/surfboards', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)

    surfboard = {
        "id": nextId, 
        "Make": request.json["Make"], 
        "Model": request.json["Model"], 
        "Type": request.json["Type"], 
        "Price": request.json["Price"]
    }
    surfboards.append(surfboard)
    nextId += 1
    return jsonify(surfboard)
    return "served by create"

#Update
#  curl -X PUT -H "content-type:application/json" -d "{\"Make\":\"Myboards\",\"Model\":\"Bestboard\",\"Type\":\"Fish\",\"Price\":9999999}" http://127.0.0.1:5000/surfboards/1
@app.route('/surfboards/<int:id>', methods=['PUT'])
def update(id):
    foundSurfboard = list(filter(lambda t : t["id"]== id, surfboards))
    if len(foundSurfboard) == 0:
        return jsonify({}), 404
    currentSurfboard = foundSurfboard[0]
    if 'Make' in request.json:
        currentSurfboard['Make'] = request.json['Make']
    if 'Model' in request.json:
        currentSurfboard['Model'] = request.json['Model']
    if 'Type' in request.json:
        currentSurfboard['Type'] = request.json['Type']
    if 'Price' in request.json:
        currentSurfboard['Price'] = request.json['Price']
    
    return jsonify(currentSurfboard)

#Delete
@app.route('/surfboards/<int:id>', methods=['DELETE'])
def delete(id):
    foundSurfboard = list(filter(lambda t : t["id"]== id, surfboards))
    if len(foundSurfboard) == 0:
        return jsonify({}), 404
    surfboards.remove(foundSurfboard[0])
   
    return jsonify({"Done":True})

if __name__ == "__main__":
    print("in if")
    app.run(debug=True)