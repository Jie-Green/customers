from db_config import Customer

# インスタンスを作成してから保存
customer = Customer(name="Bob", age="15")
customer.save()

Customer.create(name="Tom", age="57")
Customer.create(name="Ken", age="73")