import pandas as pd
import json
import os.path
import time
import random

import warnings
warnings.filterwarnings(action= 'ignore', category=FutureWarning)

available_products = {1001: {"name": "Tequila", "price": 10,
							"category": "Spirits",
							"quantity": 46, "date": "01/10/2022"},
					1002: {"name": "Gin", "price": 12,
							"category": "Spirits",
							"quantity": 46,
							"date": "01/10/2022"},
					1003: {"name": "Cognac", "price": 15,
							"category": "Spirits",
							"quantity": 46, "date": "10/10/2022"},
					1004: {"name": "Scotch Whiskey", "price": 20,
							"category": "Spirits",
							"quantity": 23, "date": "01/10/2022"},
					1005: {"name": "Negroni", "price": 24,
							"category": "Cocktails",
							"quantity": 15,
							"date": "01/10/2022"},
					1006: {"name": "Margarita", "price": 21,
							"category": "Cocktails",
							"quantity": 15, "date": "01/10/2022"},
					1007: {"name": "Rob Roy", "price": 25,
							"category": "Cocktails",
							"quantity": 10,
							"date": "01/10/2022"},
					1008: {"name": "Wagyu Steak", "price": 40,
							"category": "Food",
							"quantity": 10, "date": "01/10/2022"},
					1009: {"name": "Caeser Salad", "price": 30,
							"category": "Food",
							"quantity": 50, "date": "01/10/2022"},
					1010: {"name": "Fries", "price": 9,
							"category": "Food", "quantity": 30,
							"date": "01/10/2022"},
					}


js = json.dumps(available_products)
js
fd = open("data.json", 'w')
fd.write(js) 
fd.close()

def back_of_house():
	print("----------Welcome to Back of House for Bar Ace----------")
	while (1):
		print("1)Display All Food/Beverage Products")
		print("2)Display Specific Product")
		print("3)New Product")
		print("4)Update Product")
		print("5)Remove Product/s")
		print("6)Return")
		print("Enter Your Choice :- ")
		n = int(input())
		if (n == 1):
			display_products()
		elif (n == 2):
			display_specific_data()
		elif (n == 3):
			add_new()
		elif (n == 4):
			update_prod_data()
		elif (n == 5):
			delete_prod()
		elif (n == 6):
			break
		else:
			print("Invalid Choice...!!!")

def display_products():

	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	
	table = pd.DataFrame(columns=['ID', 'name', 'price', 'category','quantity', 'date'])
	cat = []
		
	for i in data.keys():
		temp = pd.DataFrame(columns=['ID'])
		temp['ID'] = [i]
		for j in data[i].keys():
			temp[j] = [data[i][j]]
			if (j == 'category'):
				cat.append(data[i][j])
		table = table.append(temp)
		table = table.reset_index(drop=True)
		cat = set(cat)
		cat = list(cat)
			
	for k in cat:
		temp = pd.DataFrame()
		temp = table[table['category'] == k]
		print("Data Of Products Of Category "+k+" is:- ")
		from IPython.display import display
		display(temp)

def display_specific_data():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter Product ID :- ")
	i = input()
	
	if i in data.keys():
		temp = pd.DataFrame(columns=['ID'])
		temp['ID'] = [i]
		for j in data[i].keys():
			temp[j] = [data[i][j]]
		from IPython.display import display
		display(temp)
	else:
		print("Error. The Product you entered does not exist.")

def add_new():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter New Product ID :- ")
	id = input()
	
	if id not in data.keys():
		print("Product Name :- ")
		name = input()
		print("Price :- ")
		price = input()
		print("Category :- ")
		category = input()
		print("Quantity on hand (No. of standard serves) :- ")
		quantity = input()
		print("Delivery Date :- ")
		date = input()
		data[id] = {'name': name, 'price': price,
					'category': category, 'quantity': quantity, 'date': date}
		print("Press '1' if you are ready to proceed, press '0' to modify further :- ")
		z = int(input())
		if(z == 0):
			for i in range(n):
				print("Enter Attribute Name That you Want To Change :- ")
				nam = input()
				print("Enter The "+str(nam)+" of Product :- ")
				pro = input()
				data[id][nam] = pro
		print("Product ID "+str(id)+" Added Successfully")
		
	else:
		print("The Product ID you Entered Already Exists, Please try again.")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
def delete_prod():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter The Product ID :- ")
	temp = input()
	if temp in data.keys():
		data.pop(temp)
		print("Product ID "+str(temp)+" Successfully Removed")
	else:
		print("Invalid Product ID")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
def update_prod_data():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter The ID of The Product You Want To Update :- ")
	temp = input()
	
	if temp in data.keys():
		print("To Update all Data press '0', to Update Specific Data press '1' :- ")
		q = int(input())
		
		if (q == 0):
			print("Product Name :- ")
			name = input()
			print("Price :- ")
			price = input()
			print("Category :- ")
			category = input()
			print("How many on hand :- ")
			quantity = input()
			print("Delivery Date :- ")
			date = input()
			data[temp] = {'name': name, 'price': price,'category': category, 'quantity': quantity,'date': date}
			print("Press '1' if you are ready to proceed, press '0' to modify further :- ")
			z = int(input())
			
			if(z == 0):
				print("Enter Number of New Attributes/Properties of Product :- ")
				n = int(input())
				for i in range(n):
					print("Enter Attribute Name That you Want To Add :- ")
					nam = input()
					print("Enter The "+str(nam)+" of Product :- ")
					pro = input()
					data[temp][nam] = pro
			print("Product ID "+str(temp)+" Updated Successfully...!!!")
			
		elif(q == 1):
			print("Enter Which Attribute of Product You want to Update :- ")
			p = input()
			
			if p in data[temp].keys():
				print("Enter "+str(p)+" of Product :- ")
				u = input()
				data[temp][p] = u
				print("Product ID " + str(temp) + str(p) + " is Updated Successfully")
			else:
				print("Invalid Product Attribute")
		else:
			print("Invalid Choice")
	else:
		print("Invalid Product ID")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
def display_sales_reports():
	if (os.path.isfile("user_data.json") is False):
		print("No Sales Reports are Present")
		return
	fd = open("user_data.json", 'r')
	txt = fd.read()
	user_data = json.loads(txt)
	fd.close()
	table = pd.DataFrame()
	for i in user_data.keys():
		temp = pd.DataFrame()
		for j in user_data[i].keys():
			d = dict()
			d['User ID'] = i
			d['Purchase Number'] = j
			for k in user_data[i][j].keys():
				d[k] = user_data[i][j][k]
			temp = temp.append(d, ignore_index=True)
			d = dict()
		table = table.append(temp)
	table = table.reset_index(drop=True)
	from IPython.display import display
	display(table)

def delete_all():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	data = {} 
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()

def sales_dashboard():
        print("Please Enter Four Digit Passcode :-")
        k = int(input())
        
        if (k == 9999):
                print("----------Welcome to Bar Ace's Sales Dashboard----------")
                while (1):
                        print("1)Sales History")
                        print("2)Enter Sales Data")
                        print("3)Exit")
                        print("Enter Your Choice :- ")
                        n = int(input())
                        if (n == 1):
                                display_sales_reports()
                        elif (n == 2):
                                input_sales()
                        elif (n == 3):
                                break
                        else:
                                print("Invalid Choice...!!!")
        else:
                        print("Incorrect Password")

def generate_bill(user_id, prod_id, price, time_date, purchase_no,
				name, category, quantity_all, transaction_id):
	print("========= Sales Summary ========")
	print("#######################")
	print(" Manager Password :-", user_id)
	print("#################")
	amount = 0
	n = len(purchase_no)
	
	for i in range(n):
		print("-----------------------------------------")
		amount = amount+float(price[i])*float(quantity_all[i])
		print("Purchase number", purchase_no[i],
			"\nPurchase Time :-", time_date[i], "\nProduct ID :-",
			prod_id[i], "\nName Of Product :-",
			name[i], "\nCategory Of Product :-", category[i],
			"\nPrice of Product per Item :-", price[i],
			"\nPurchase Quantity :-", quantity_all[i])
		print("-----------------------------------")
	print("*****************************************")
	print(" Total Revenue :-",
		amount, "Close of Business ID :-", transaction_id)
	print("***************************************")


def input_sales():
	
	if (os.path.isfile("user_data.json") is False):
		user_data = {}
	else:
		fd = open("user_data.json", 'r')
		txt = fd.read()
		user_data = json.loads(txt)
		fd.close()
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Please Enter Manager Code to Proceed or Press '0' if you are new :- ")
	p = int(input())
	if (p == 0):
		if (len(user_data.keys()) == 0):
			user_id = 1000
		else:
			user_id = int(list(user_data.keys())[-1])+1
	else:
		if str(p) in user_data.keys():
			user_id = p
		else:
			user_id = -1
	if (user_id != -1):
		user_id = str(user_id)
		price = []
		time_date = []
		purchase_no = []
		name = []
		category = []
		quantity_all = []
		prod_id = []
		transaction_id = ''.join(random.choice(
			'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
		print("How many products did you sell this evening? :- ")
		n = int(input())
		print("Enter Data As Follows :- ")
		if user_id not in user_data.keys():
			user_data[user_id] = {}
			g = 0
		else:
			g = int(list(user_data[user_id].keys())[-1])+1
		for i in range(n):
			print("Enter Product ID of Product " +
				str(i+1)+" that you sold")
			id = input()
			if id in data.keys():
				user_data[user_id][str(i+1+g)] = {}
				user_data[user_id][str(i+1+g)]['time_date'] = str(time.ctime())
				time_date.append(str(time.ctime()))
				if(float(data[id]['quantity']) == 0.0):
					print("Invalid entry. Product amount is larger than what is on hand.")
					continue
				purchase_no.append(i+1+g)
				name.append(data[id]['name'])
				user_data[user_id][str(i+1+g)]['name'] = data[id]['name']
				prod_id.append(id)
				user_data[user_id][str(i+1+g)]['product_id'] = id
				category.append(data[id]['category'])
				user_data[user_id][str(
					i+1+g)]['category'] = data[id]['category']
				print("For Product " + str(data[id]['name']) + " amount on Hand is :- "+str(data[id]['quantity']))
				print("Enter Quantity of Product "+ str(i+1) +" that was sold")
				quantity = input()
				if (float(quantity) <= float(data[id]['quantity'])):
					data[id]['quantity'] = str(float(data[id]['quantity'])-float(quantity))
					quantity_all.append(quantity)
					user_data[user_id][str(i+1+g)]['quantity'] = str(quantity)
					price.append(data[id]['price'])
					user_data[user_id][str(i+1+g)]['price'] = data[id]['price']
					user_data[user_id][str(i+1+g)]['Transaction ID'] = str(transaction_id)
				else:
					print("Error. Quantity input is larger than what is currently on hand")
					print("Press '0' to input sales, press '1' to skip product")
					key = int(input())
					if (key == 0):
						print("Enter Quantity of Product " +str(i+1)+ " Sold")
						quantity = intput()
						if (float(quantity) <= float(data[id]['quantity'])):
							data[id]['quantity'] = str(float(data[id]['quantity'])-float(quantity))
							quantity_all.append(quantity)
							user_data[user_id][str(i+1)]['quantity'] = str(quantity)
							price.append(data[id]['price'])
							user_data[user_id][str(i+1)]['price'] = data[id]['price']
							user_data[user_id][str(i+1+g)]['Transaction ID'] = str(transaction_id)
						else:
							print("Error. Input Invalid.")
					elif (key == 1):
						continue
					else:
						print("Error. Input Invalid.")
			else:
				print("Invalid Product ID...!!!")
		if(len(purchase_no) != 0):
			generate_bill(user_id, prod_id, price, time_date, purchase_no,name, category, quantity_all, transaction_id)
	else:
		print("Error. Manager Profile does not exist")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	js = json.dumps(user_data)
	fd = open("user_data.json", 'w')
	fd.write(js)
	fd.close()


while (1):
        print("----------Welcome to Bar Ace's Venue Management System----------")
        print("How would you like to proceed? :- ")
        print("1)Back of House")
        print("2)Sales Dashboard")
        print("3)Exit")
        print("Enter Your Choice Here :- ")
        n = int(input())
        if (n == 1):
                back_of_house()
        elif (n == 2):
                sales_dashboard()
        elif (n == 3):
                break
        else:
                print("Invalid Choice")
