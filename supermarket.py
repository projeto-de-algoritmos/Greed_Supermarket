from collections import Counter

class Supermarket():
    total = 0.0

    def get_total(self):
        return self.total

    def change_value(self, value):
        self.total += value

    def calculate_number_of_coins(self, change):
        currency = [0.01, 0.05, 0.1, 0.25, 0.5, 1.00, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0]

        n = len(currency)
        result = []
        i = n - 1
        change = round(change, 2)

        while i >= 0:
            while change >= currency[i]:
                change = round(change - currency[i],2)
                result.append(currency[i])

            i -= 1

        result = dict(Counter(result))

        for i in list(set(currency) - set(result)):
            result[i] = 0

        return result