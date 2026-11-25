customers=[
  (101,"Miller",25000),
  (102,"Allen",30000),
  (103,"Balke",35000)]
for customer in customers:
  print(customer)
print("Customer data Intehration completed")
print("New feature added successfully")

def calculate_bonus(sal):
  return sal*0.10
sal=50000
bonus=calculate_bonus(sal)
print("Employee bonus :",bonus)

def validate_customer(customer_id,customer_name):
  if customer_id <=0:
    return "Invalid customer ID"
  if not customer_name:
    return "Invalid customer name"
  return "Valid customer"

print(validate_customer(101,"Miller"))
print(validate_customer(102,""))
print(validate_customer(-1,"Allen"))