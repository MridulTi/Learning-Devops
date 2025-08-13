import argparse
import uuid
import json
import os

class Todo:
    def __init__(self):
        self.filename="todo.json"
        self.todos=self.load_file()
    
    def add(self,title,description,status=None):
        todo={
            "id": str(uuid.uuid4()),
            "title":title if title else None,
            "description": description if description else None,
            "status":status if status else "not complete",
        }
        self.todos.append(todo)
        self.save_file()
        return self.todos

    def save_file(self):
        with open(self.filename, "w") as f:
            json.dump(self.todos,f,indent=4)

    def load_file(self):
        if os.path.exists(self.filename):
            with open(self.filename,"r") as f:
                return json.load(f)
        return []

    def listt (self):
        for task in self.todos:
            print("List: ",task)
    
    def delete (self,task_id):
        for task in range(len(self.todos)):
            if (self.todos[task]["id"]==task_id):
                del self.todos[task]
                self.save_file()
                return self.todos

    def complete (self,task_id):
         for task in range(len(self.todos)):
            if (self.todos[task]["id"]==task_id):
                self.todos[task]["status"]="Complete"
                self.save_file()
                return self.todos

if __name__=="__main__":

    parser= argparse.ArgumentParser()
    subparser=parser.add_subparsers(dest="command")

    add_parser= subparser.add_parser("add")
    add_parser.add_argument('--title',required=True)
    add_parser.add_argument('--desc',required=True)

    complete_parser= subparser.add_parser("complete")
    complete_parser.add_argument('id')

    del_parser= subparser.add_parser("delete")
    del_parser.add_argument('id')

    subparser.add_parser('list')

    args=parser.parse_args()
    todo=Todo()

    if args.command == "add":
        AddList=todo.add(args.title, args.desc)
        print(AddList)
    elif args.command == "list":
        todo.listt()
    elif args.command == "complete":
        todo.complete(args.id)
    elif args.command == "delete":
        todo.delete(args.id)
    else:
        print("Invalid command. Use --help for options.")

