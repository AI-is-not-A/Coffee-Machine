class CoffeeMachine:
    COFFEE_TYPES = "expresso", "latte", "cappuccino"
    INGREDIENTS = ("water", "ml"), ("milk", "ml"), ("coffee beans", "g")

    def __init__(self):
        self.options = "buy", "fill", "take"
        # [water (ml), milk (ml), coffee beans (g), price ($)]
        self.coffees = {self.COFFEE_TYPES[0]: [250, 0, 16, 4],
                        self.COFFEE_TYPES[1]: [350, 75, 20, 7],
                        self.COFFEE_TYPES[2]: [200, 100, 12, 6]}

        self.ingredients_amount = [400, 540, 120]
        self.money_amount_dollars = 550
        self.cups = 9

        while True:
            action = input("Write action (buy, fill, take, remaining, exit): \n").lower().strip()
            print("\r")
            if action == "exit":
                break
            self.process_action(action)
            print("\r")

    def process_action(self, selected_option):
        if selected_option == "buy":
            user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n")
            if user_input != "back" and self.check_resources(int(user_input) - 1):
                self.make_coffee(int(user_input) - 1)

        elif selected_option == "fill":
            for i in range(3):
                self.ingredients_amount[i] += int(input(
                    f"Write how many {"grams" if i == 2 else self.INGREDIENTS[i][1]} "
                    f"of {self.INGREDIENTS[i][0]} you want to add: \n"))
            self.cups += int(input(f"Write how many disposable cups you want to add: \nf"))

        elif selected_option == "take":
            print(f"I gave you ${self.money_amount_dollars}")
            self.money_amount_dollars = 0

        elif selected_option == "remaining":
            self.print_machines_state()

    def print_machines_state(self):
        print("The coffee machine has:")
        for i in range(0, 3):
            print(f"{self.ingredients_amount[i]} {self.INGREDIENTS[i][1]} of {self.INGREDIENTS[i][0]}")
        print(f"{self.cups} disposable cups\n"
              f"${self.money_amount_dollars} of money")

    def check_resources(self, coffee_type_index):
        for i in range(0, 3):
            if self.ingredients_amount[i] < self.coffees[self.COFFEE_TYPES[coffee_type_index]][i]:
                print(f"Sorry, not enough {self.INGREDIENTS[i][0]}!")
                return False
        if self.cups == 0:
            print("Sorry, not enough cups!")
            return False
        print("I have enough resources, making you a coffee!")
        return True

    def make_coffee(self, coffee_type_index):
        self.ingredients_amount = list(map(lambda x, y: x - y,
                                           self.ingredients_amount,
                                           self.coffees[self.COFFEE_TYPES[coffee_type_index]]))
        self.money_amount_dollars += self.coffees[self.COFFEE_TYPES[coffee_type_index]][3]
        self.cups -= 1


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
