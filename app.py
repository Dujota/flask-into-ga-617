# app.py
from flask import Flask, abort, request
app = Flask(__name__)

personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/information')
def information():
    # find the recond in the database
    #do somehtin that with at record
    #convert to json
    #return the json to the requestor
    return 'This is another endpoint, normally we would send json'

@app.route('/profile/<name>')
def profile(name):
  return f"This is the profile information for {name.upper()}"

@app.route('/personnel/<name>')
def employee(name):
    person_position = personnel.get(name)

    if person_position:
      return person_position
    else:
      abort(404)


@app.route('/employee-search')
def employee_search():
  # print(request.args)
  name = request.args.get("name")
  age = request.args.get("age")
  return f"I searched for employees named {name} who are {age} years old"

if __name__ == '__main__':
    app.run()


# :id
# req.params.id

# <id>
# id

# /search?term=cats
# req.query.term ==> "cats"
# request.args.get("term") ===> "cats"