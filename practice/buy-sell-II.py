class buy_sell:
    def solution(self, trades)->int:
        profit = 0 
        for position in range(1, len(trades)):
            if trades[position]> trades[position-1]:
                profit += trades[position] - trades[position-1] 
        return profit

bs = buy_sell()
print(bs.solution([7,1,5,3,6,4])     )