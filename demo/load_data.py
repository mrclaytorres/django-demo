from demo.models import Product
import csv

def run():
  with open('demo/demo.csv') as file:
    reader = csv.reader(file)
    next(reader) # Advanced past the header

    Product.objects.all().delete()

    for row in reader:
      print(row)

      product = Product(sku=row[0],
                        name=row[1],
                        brand=row[2])
      
      product.save()