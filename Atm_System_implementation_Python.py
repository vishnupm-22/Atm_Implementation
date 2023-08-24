class Atm:
    def __init__(self):
        self.__pin = None
        self.__balance = 0
        self.__attempts = 0
        self.__max_attempts = 3
        self.menu()

    def menu(self):
        while True:
            if bank is None:
                print("Please select a bank first.")
                break

            user_input = input('''
            Hello, how would you like to proceed:
            1. Enter 1 to Create PIN
            2. Enter 2 to Deposit
            3. Enter 3 to Withdraw
            4. Enter 4 to Check Balance
            5. Enter 5 to Exit\n''')

            if user_input == '1':
                if self.__pin is None:
                    self.create_pin()
                else:
                    print("PIN has already been set.")
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                if bank is not None:
                    print("Exiting...")
                else:
                    print("Please select a bank first.")
                break
            else:
                print("Invalid input")

    def create_pin(self):
        self.__pin = input("Enter your new PIN: ")
        print("ATM PIN created successfully")

    # Getter method for __pin
    def get_pin(self):
        return self.__pin

    # Setter method for __pin
    def set_pin(self, new_pin):
        self.__pin = new_pin

    def withdraw(self):
        if self.authenticate():
            amount = self.get_amount_input("Enter the amount to withdraw: ")
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
            else:
                print("Not enough funds in the account")

    def deposit(self):
        if self.authenticate():
            amount = self.get_amount_input("Enter the amount to deposit: ")
            self.__balance += amount
            print("Deposit successful")

    def check_balance(self):
        if self.authenticate():
            print("Current balance:", self.__balance)

    def authenticate(self):
        if self.__attempts >= self.__max_attempts:
            print("Too many incorrect attempts. Please contact customer support.")
            return False

        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            self.__attempts = 0
            return True
        else:
            self.__attempts += 1
            print("Incorrect PIN")
            print("Attempts left:", self.__max_attempts - self.__attempts)
            return False

    @staticmethod
    def get_amount_input(prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount < 0:
                    print("Amount cannot be negative")
                else:
                    return amount
            except ValueError:
                print("Invalid input. Please enter a valid amount.")


while True:
    bank = None

    while bank is None:
        bank = int(input('''Hello, with which bank account would you like to continue:
                1. SBI
                2. Canara
                3. ICICI
                4. AXIS
                5. Exit\n'''))

        if bank == 5:
            print("Exiting...")
            break
        elif bank not in [1, 2, 3, 4]:
            print("Invalid input, please select from the mentioned options.")
            bank = None

        if bank == 1:
            print("Your SBI account is created.")
            SBI = Atm()
        elif bank == 2:
            print("Your Canara account is created.")
            CANARA = Atm()
        elif bank == 3:
            print("Your ICICI account is created.")
            ICICI = Atm()
        elif bank == 4:
            print("Your Axis account is created.")
            AXIS = Atm()