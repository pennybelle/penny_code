class Multiplier():
    answer = 0
    def solve(number=int(input('input:')), multiplier=int(input('times:'))):
        for i in range(0, multiplier):
            Multiplier.answer += number
        return Multiplier.answer

print(Multiplier.solve())