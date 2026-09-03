class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, unit):
        return self          # ยังไม่มีการแปลงหน่วย จึงคืนตัวเอง

    def __eq__(self, other):
        return (isinstance(other, Quantity)
                and self.amount == other.amount
                and self.unit == other.unit)

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, unit):
        amount = self.left.reduce(unit).amount + self.right.reduce(unit).amount
        return Quantity(amount, unit)


class Converter:
    def reduce(self, source, unit):
        return source.reduce(unit)


def grams(amount):
    return Quantity(amount, "g")