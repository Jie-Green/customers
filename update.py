from db_config import Customer


def display_all_customer():
    for customer in Customer.select():
        print(customer.id, customer.name)


def update_customer(id):
    customer = Customer.get_by_id(id)
    customer.name = "Tom Ford"
    customer.save()


if __name__ == "__main__":
    display_all_customer()

    id = 3
    customer = Customer.get_by_id(id)
    customer.user = "Tom Ford"
    customer.save()
    update_customer(id)

    display_all_customer()
