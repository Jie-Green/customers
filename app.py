from db_config import Customer


def select():
    print("===== Welcome to CRM Application =====")
    print("[S]how: Show all users info")
    print("[A]dd: Add new user")
    print("[Q]uit: Quit The Application")
    print("======================================")
    print()


def add():
    user_name = input("New user name >")
    user_age = input("New user age >")

    customer = Customer(name=user_name, age=user_age)
    customer.save()
    print(f"Add new user:{user_name}")


def show():
    for customer in Customer.select():
        print(f"Name: {customer.name} Age: {customer.age}")


def finish():
    print("Bye!")


select()


def main():
    while True:
        select = input("Your command > ")

        if select == "S":
            show()
            continue

        if select == "A":
            add()
            continue

        if select == "Q":
            finish()
            break

        print("command not found")


if __name__ == "__main__":
    main()
