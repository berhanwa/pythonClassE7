
def find_largest_increase ():
    max_increase = 0
    start_day = 0
    end_day = 0

    for day in range (1,11):
        price = int(input(f"Enter stock price for day {day}: "))

        if day > 1:
            increase = price - prev_price
            if increase > max_increase
                start_day = day - 1
                end_day = day

                prev_price = price
