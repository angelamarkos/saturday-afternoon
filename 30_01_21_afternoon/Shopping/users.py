class User:
    def __init__(self, email, password, full_name, gender, birth_date):
        self.email = email
        self.__password = password
        self.full_name = full_name
        self.gender = gender
        self.birth_date = birth_date

    def login(self):
        pass

    def update_info(self, *args):
        pass

    def update_password(self, value):
        self.__password = value

class Customer(User):
    def __init__(self, email, password, full_name, gender,
                 birth_date, card, billing_address, shipping_address, currency):
        super().__init__(email, password, full_name, gender, birth_date)
        self.card = card
        self.billing_address = billing_address
        self.shipping_address = shipping_address
        self.currency = currency

    def add_card(self, card):
        pass

    def add_product(self, product):
        pass


class VipCustomer(Customer):
    def __init__(self, email, password, full_name, gender,
                 birth_date, card, billing_address, shipping_address, currency,
                 discount, free_shippinng, cupon):
        super().__init__(self, email, password, full_name, gender,
                 birth_date, card, billing_address, shipping_address, currency)

        self.discount = discount
        self.free_shipping = free_shippinng
        self.cupon = cupon

    def use_cupon(self):
        pass



class Admin(User):
    def __init__(self, user, department):

        self.department = department

    def add_product(self):
        pass
        

class Cart:
    def __init__(self, cardholder_name, card_number, expiration_date, cvv_cvc):
        self.cardholder_name = cardholder_name
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv_cvc = cvv_cvc

    def to_string(self):
        pass

class Address:
    def __init__(self):
        pass

    def to_string(self):
        pass



