
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def moneyX(self):
        try:
            amount = float(input('Введите сумму для пополнения счета:'))
            if amount > 0:
                self.balance += amount
                print(f'Сумма {amount} успешно пополнили счет.')
            else:
                print('Пожалуйста введите положительную сумму.')
        except ValueError:
            print('Пожалуйста введите корректную число.')


    def kill(self):
        self.balance = 0
        print("Баланс обнулен.")


    def jackpot(self):
        self.balance *= 10
        print("Джекпот! Ваш баланс умножен на 10.")

    def join_balances(self, other_account):
        if isinstance(other_account, Bank):
            self.balance += other_account.get_balance()
            print("Балансы успешно объединены!")
        else:
            print("Ошибка! Невозможно объединить баланс с объектом другого класса.")

client1 = Bank("Клиент1", 100)
client2 = Bank("Клиент2", 200)

client1.moneyX()

client1.kill()

client1.jackpot()

client1.join_balances(client2)

print(f"Баланс Клиента1: {client1.get_balance()}")

