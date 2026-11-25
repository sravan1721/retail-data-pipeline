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
