from flask import Flask, url_for, request, redirect, abort, jsonify
from EmployeeDao import employeeDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
#get all


@app.route('/employees')
def getAll():
    return jsonify(employeeDao.getAll())
# find By id


@app.route('/employees/<int:EMPID>')
def findById(EMPID):
    return jsonify(employeeDao.findById(EMPID))

# create



@app.route('/employees', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    employee = {
        "EMPID": request.json["EMPID"],
        "First_Name": request.json["First_Name"],
        "Last_Name": request.json["Last_Name"],
        "DEPCODE": request.json["DEPCODE"],
        "ADDR1": request.json["ADDR1"],
        "CITY": request.json["CITY"],
        "STATE": request.json["STATE"],
        "ZIP": request.json["ZIP"]
    }
    return jsonify(employeeDao.create(employee))

    return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/employees/1


@app.route('/employees/<int:EMPID>', methods=['PUT'])
def update(EMPID):
    foundEmployee=employeeDao.findById(EMPID)
    print (foundEmployee)
    if foundEmployee == {}:
        return jsonify({}), 404
    currentEmployee = foundEmployee
    if 'First_Name' in request.json:
        currentEmployee['First_Name'] = request.json['First_Name']
    if 'Last_Name' in request.json:
        currentEmployee['Last_Name'] = request.json['Last_Name']
    if 'DEPCODE' in request.json:
        currentEmployee['DEPCODE'] = request.json['DEPCODE']
    if 'ADDR1' in request.json:
        currentEmployee['ADDR1'] = request.json['ADDR1']
    if 'CITY' in request.json:
        currentEmployee['CITY'] = request.json['CITY']
    if 'STATE' in request.json:
        currentEmployee['STATE'] = request.json['STATE']
    if 'ZIP' in request.json:
        currentEmployee['ZIP'] = request.json['ZIP']
    employeeDao.update(currentEmployee)

    return jsonify(currentEmployee)

#delete
# curl -X DELETE http://127.0.0.1:5000/employees/1


@app.route('/employees/<int:EMPID>', methods=['DELETE'])
def delete(EMPID):
    employeeDao.delete(EMPID)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)