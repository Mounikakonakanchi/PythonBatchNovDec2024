"""
Purpose: Grocery Store

item            cost
----
rice             10/kg
Wheat           34/kg

Algorithm:
step1: Get the cost of item into variables
step2: Get the quantity of item from the user 

Note: input(), to get the values in runtime.

"""
cost_of_rice = 10 #per kg
cost_of_wheat = 34 #per kg

#quantity of items

qty_of_rice=input("Enter qty of rice(in kgs) :")
qty_of_rice = float(qty_of_rice)
print("Qty Of Rice :",qty_of_rice, type(qty_of_rice))


qty_of_wheat=input("Enter qty of wheat(in kgs) :")
qty_of_wheat = float(input("Enter Qty. of wheat(in kgs) :"))


#Selling price computation 
sp_of_rice = cost_of_rice * qty_of_rice
print("Sp of Rice :",sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("Sp of Wheat :",sp_of_wheat)

total_sp= sp_of_rice + sp_of_wheat
print("Total Sp :",total_sp)
