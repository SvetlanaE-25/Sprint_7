import random
import string



def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_order_dict(color=None):
    first_name = generate_random_string(6)
    last_name = generate_random_string(8)
    address = generate_random_string(10)
    metro_station = random.randint(1, 200)
    phone = f"+7{random.randint(1000000000, 9999999999)}"
    rent_time = random.randint(1, 7)
    delivery_date = "2026-06-12"
    comment = generate_random_string(15)

    order_data = {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": delivery_date,
        "comment": comment
    }

    if color is not None:
        order_data["color"] = color

    return order_data