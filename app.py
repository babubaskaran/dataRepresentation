from flask import Flask, url_for, request, redirect, abort, jsonify
from EmployeeDao import employeeDao
from DepartmenDao import departmenDao

app = Flask(__name__, static_url_path="", static_folder="staticpages")


@app.route("/")
def index():
    return "hello"


# get all


@app.route("/employees")
def getAll():
    return jsonify(employeeDao.getAll())


# find By id


@app.route("/employees/<int:EMPID>")
def findById(EMPID):
    return jsonify(employeeDao.findById(EMPID))


# create


@app.route("/employees", methods=["POST"])
def create():
    if not request.json:
        abort(400)

    employee = {
        "EMPID": request.json["EMPID"],
        "FirstName": request.json["FirstName"],
        "LastName": request.json["LastName"],
        "DEPCODE": request.json["DEPCODE"],
        "ADDR1": request.json["ADDR1"],
        "CITY": request.json["CITY"],
        "STATE": request.json["STATE"],
        "ZIP": request.json["ZIP"],
    }
    return jsonify(employeeDao.create(employee))

    return "served by Create "


# update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/employees/1


@app.route("/employees/<int:EMPID>", methods=["PUT"])
def update(EMPID):
    foundEmployee = employeeDao.findById(EMPID)
    print(foundEmployee)
    if foundEmployee == {}:
        return jsonify({}), 404
    currentEmployee = foundEmployee
    if "FirstName" in request.json:
        currentEmployee["FirstName"] = request.json["FirstName"]
    if "LastName" in request.json:
        currentEmployee["LastName"] = request.json["LastName"]
    if "DEPCODE" in request.json:
        currentEmployee["DEPCODE"] = request.json["DEPCODE"]
    if "ADDR1" in request.json:
        currentEmployee["ADDR1"] = request.json["ADDR1"]
    if "CITY" in request.json:
        currentEmployee["CITY"] = request.json["CITY"]
    if "STATE" in request.json:
        currentEmployee["STATE"] = request.json["STATE"]
    if "ZIP" in request.json:
        currentEmployee["ZIP"] = request.json["ZIP"]
    employeeDao.update(currentEmployee)

    return jsonify(currentEmployee)


# delete
# curl -X DELETE http://127.0.0.1:5000/employees/1


@app.route("/employees/<int:EMPID>", methods=["DELETE"])
def delete(EMPID):
    employeeDao.delete(EMPID)

    return jsonify({"done": True})


# ============================================= Start: department =================================================

# get all


@app.route("/department")
def getAllDept():
    return jsonify(departmenDao.getAllDept())


# find By id


@app.route("/department/<int:DEPCODE>")
def findById2Dept(DEPCODE):
    return jsonify(departmenDao.findById2Dept(DEPCODE))


# create


@app.route("/department", methods=["GET", "POST"])
def create2Dept():
    if not request.json:
        abort(400)

    departmen = {
        "DEPCODE": request.json["DEPCODE"],
        "DeptName": request.json["DeptName"],
        "MGR_Name": request.json["MGR_Name"]
    }
    return jsonify(departmenDao.create2Dept(departmen))

    return "served by Create2 "


# update
@app.route("/department/<int:DEPCODE>", methods=["PUT"])
def updateDept(DEPCODE):
    foundDepartmen = departmenDao.findById2Dept(DEPCODE)
    print(foundDepartmen)
    if foundDepartmen == {}:
        return jsonify({}), 404
    currentDepartmen = foundDepartmen
    if "DeptName" in request.json:
        currentDepartmen["DeptName"] = request.json["DeptName"]
    if "MGR_Name" in request.json:
        currentDepartmen["MGR_Name"] = request.json["MGR_Name"]
    departmenDao.updateDept(currentDepartmen)

    return jsonify(currentDepartmen)


# delete


@app.route("/department/<int:DEPCODE>", methods=["DELETE"])
def deleteDept(DEPCODE):
    departmenDao.deleteDept(DEPCODE)

    return jsonify({"done": True})

# ============================================= End: department =================================================

if __name__ == "__main__":
    app.run(debug=True)
