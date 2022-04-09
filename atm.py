class atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your balance is: $100") 

    def cashwidrawal(self, amount):
        new_amount = 100 - amount
        print("You have withdrawn: $", amount)

def main():
    name = input("Emter your name: ")
    print("Hello", name)
    cardnumber = input("Enter your card number: ")
    pin = input("Enter your pin: ")
    new_user = atm(cardnumber, pin)

    print("1. Balance inquiry")
    print("2. Cash withdrawal")
    activity = int(input("Enter your activity, choose either 1 or 2: "))

    if activity == 1:
        new_user.balanceinquiry()
    elif activity == 2:
        amount = int(input("Enter the amount you want to withdraw: "))
        print("You have withdrawn: $", amount, "now you have left over with: $", 100 - amount)
    else:
        print("Invalid activity")

if __name__ == "__main__":
    main()