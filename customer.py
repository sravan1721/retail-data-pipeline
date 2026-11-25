def validate_cust(customer_id,customer_name):
  if customer_id <=0:
    return False
  if not customer_name:
    return False
  return True
def calculate_discount(amount):
  if amount >=5000:
    return amount *0.10
  return amount *0.05
