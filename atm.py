class Machine(object):

    def __init__(self):
        self.stored_money = 1000
        self.members = [
            {
                'name': 'Kurdapyo Cholo',
                'pin': 6996,
                'balance': 300
            },
            {
                'name': 'Ben Dover',
                'pin': 1111,
                'balance': 500
            },
            {
                'name': 'King Kalis',
                'pin': 2222,
                'balance': 0
            },
            {
                'name': 'George Kaba',
                'pin': 666,
                'balance': 1500
            }
        ]

        self.actions = {
            1: {
                'text':'1.) Balance Inquiry',
                'action': self.balance_inquire,
            },
            2: {
                'text':'2.) Withdraw Moneys',
                'action': self.withdraw_money,
            },
            3: {
                'text':'3.) DIE ATM',
                'action': self.exit,
            },
        }


    def greet(self):
        print("-"*10)
        print("Good Morning, I am ATM")
        print("-"*10)

    def select_actions(self):
        print('_'*20)
        print("I currently have {}".format(self.stored_money))
        
        # Print all actions
        for key, value in self.actions.items():
            print(value['text'])

        # Select action
        user_action = int(input("Wacha wanna do?: "))
        print('^'*20)

        self.actions[user_action]['action']()

    def exit(self):
        return False

    def get_member(self):
        pin = int(input("Please enter your pin: "))

        selected_member = None;

        for member in self.members:
            if member['pin'] == pin:
                selected_member = member

        return selected_member

    def withdraw_money(self):
        selected_member = self.get_member()
        
        if selected_member:
            amt = int(input("How much u want?: "))

            index = self.members.index(selected_member)

            if amt > self.stored_money:
                print("Dong, wa na koy kwarta. Gamay gamay lang sa.")
                return

            if amt > selected_member['balance']:
                print("Dong, wa kay kwarta. Insufficient do.")
                return

            # Reduce member's balance
            self.members[index]['balance'] -= amt
            print("Giving u {} moneys".format(amt))
            print("Ur current balance is: {}".format(self.members[index]['balance']))

            self.stored_money -= amt
            return

    def balance_inquire(self):
        selected_member = self.get_member()

        if selected_member:
            print("Hello {}, your balance is: {}".format(selected_member['name'], selected_member['balance']))
        else:
            print("WHO U, SCAMMZ")
        return


    def start_machine(self):
        running = True
        
        while running:
            running = self.select_actions()
