order = {
    "id" : "12345", 
    "product_no" : "FP123",
    "productname" : "Fluffy Pillow",
    "price" : "39.99"
  }

for x in order:
   print (order[x])

order.update({"id": "12346"})

for x in order:
   print (order[x])