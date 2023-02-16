import json


class Todos:
  from flask import request

@app.route("/api/v1/todos/", methods=["POST"])
def create_todo():
    if not request.json or not 'title' in request.json:
      abort(400)
todo = {
    'id': todos.all()[-1]['id'] + 1,
    'title': request.json['title'],
    'description': request.json.get('description', ""),
    'done': False
  }
todos.create(todo)

def __init__(self):
    try:
      with open("todos.json", "r") asf:
        self.todos = json.load(f)
    except FileNotFoundError:
      self.todos = []

def all(self):
    return self.todos

def get(self, id):
    return self.todos[id]

def create(self, data):
  self.todos.append(data)
  self.save_all()


def delete(self, id):
  todo = self.get(id)
  if todo:
    self.todos.remove(todo)
    self.save_all()
    return True
  return False

def save_all(self):
    with open("todos.json", "w") as f:
      json.dump(self.todos, f)

def update(self, id, data):
  todo = self.get(id)
  if todo:
    index = self.todos.index(todo)
    self.todos[index] = data
    self.save_all()
    return True
  return False

todos = Todos()