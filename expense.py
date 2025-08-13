import argparse
import os
import csv

class Expense:
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    
    def display(self):
        return {"Name":self.name,"Amount":self.amount}

class ExpenseManager:
    def __init__(self):
        self.filename="expense.csv"

    def display(self):
        with open(self.filename ,"r") as file:
            reader=csv.reader(file)
            for data in reader:
                print(', '.join(data))

    def add(self,name,amount):
        with open(self.filename,"a") as file:
            writer=csv.writer(file, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            expense=Expense(name,amount)
            writer.writerow("Expense: "+str(expense.display()))


if __name__=="__main__":

    parser=argparse.ArgumentParser()
    subparser=parser.add_subparsers(dest='command')

    add_parser=subparser.add_parser('add')
    add_parser.add_argument('--name',required=True)
    add_parser.add_argument('--amount',required=True)

    subparser.add_parser('list')

    args=parser.parse_args()

    expMan=ExpenseManager()

    if args.command=="add":
        expMan.add(args.name,args.amount)
    elif args.command=="list":
        expMan.display()
