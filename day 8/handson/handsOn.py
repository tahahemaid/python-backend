
class Payment:
    def __init__(self, amount):
        self._amount = amount
        self.__status = "Pending"
    def process(self):
  
        raise NotImplementedError("Subclasses must implement this method.")

    def get_status(self):
  
        return self.__status

    def _set_status(self, status):

        self.__status = status

    def __str__(self):
        return f"Payment of ${self._amount:.2f} - Status: {self.__status}"

    def __repr__(self):
        return f"Payment(amount={self._amount}, status='{self.__status}')"

    def __add__(self, other):
        """
        Magic method to sum payments.
        """
        if isinstance(other, Payment):
            return Payment(self._amount + other._amount)
        return NotImplemented


class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        print(f"Processing credit card payment of ${self._amount:.2f}...")
        self._set_status("Completed")  


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):

        print(f"Processing PayPal payment of ${self._amount:.2f} from {self.email}...")
        self._set_status("Completed")


def process_all_payments(payments):
    for p in payments:
        p.process() 
        print(p) 


if __name__ == "__main__":
    payment1 = CreditCardPayment(100.50, "1234-5678-9876-5432")
    payment2 = PayPalPayment(59.99, "customer@example.com")

    process_all_payments([payment1, payment2])

    combined_payment = payment1 + payment2
    print("Combined payment:", combined_payment)

    print("Payment1 status (via getter):", payment1.get_status())
