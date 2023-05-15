change = int(input())
remainder = change % 100
remainder2 = remainder % 25
remainder3 = remainder2 % 10
remainder4 = remainder3 % 5
remainder_q = change % 25
remainder_q1 = remainder_q % 10
remainder_q2 = remainder_q1 % 5
remainder_d = change % 10
remainder_d1 = remainder_d % 5
remainder_n = change % 5

if change >= 100 and (change < 200):
    print(int(change / 100), 'Dollar')
    if remainder < 50 and (remainder >= 25):
        print(int(remainder / 25), 'Quarter')
    if remainder <= 99 and (remainder >= 50):
        print(int(remainder / 25), 'Quarters')
    if remainder2 <= 19 and (remainder2 >= 10):
        print(int(remainder2 / 10), 'Dime')
    if remainder2 <= 24 and (remainder2 >= 20):
        print(int(remainder2 / 10), 'Dimes')
    if remainder3 < 10 and (remainder3 >= 5):
        print(int(remainder3 / 5), 'Nickel')
    if remainder4 < 2 and (remainder4 == 1):
        print(int(remainder4 / 1), 'Penny')
    if remainder4 <= 4 and (remainder4 >= 2):
        print(int(remainder4 / 1), 'Pennies')
elif change >= 200 and (change < 1000):
    print(int(change / 100), 'Dollars')
    if remainder < 50 and (remainder >= 25):
        print(int(remainder / 25), 'Quarter')
    if remainder <= 99 and (remainder >= 50):
        print(int(remainder / 25), 'Quarters')
    if remainder2 <= 19 and (remainder2 >= 10):
        print(int(remainder2 / 10), 'Dime')
    if remainder2 <= 24 and (remainder2 >= 20):
        print(int(remainder2 / 10), 'Dimes')
    if remainder3 < 10 and (remainder3 >= 5):
        print(int(remainder3 / 5), 'Nickel')
    if remainder4 < 2 and (remainder4 == 1):
        print(int(remainder4 / 1), 'Penny')
    if remainder4 <= 4 and (remainder4 >= 2):
        print(int(remainder4 / 1), 'Pennies')
elif change < 50 and (change >= 25):
    print(int(change / 25), 'Quarter')
    if remainder_q <= 19 and (remainder_q >= 10):
        print(int(remainder_q / 10), 'Dime')
    if remainder_q <= 24 and (remainder_q >= 20):
        print(int(remainder_q / 10), 'Dimes')
    if remainder_q1 < 10 and (remainder_q1 >= 5):
        print(int(remainder_q1 / 5), 'Nickel')
    if remainder_q2 < 2 and (remainder_q2 == 1):
        print(int(remainder_q2 / 1), 'Penny')
    if remainder_q2 <= 4 and (remainder_q2 >= 2):
        print(int(remainder_q2 / 1), 'Pennies')
elif change <= 99 and (change >= 50):
    print(int(change / 25), 'Quarters')
    if remainder_q <= 19 and (remainder_q >= 10):
        print(int(remainder_q / 10), 'Dime')
    if remainder_q <= 24 and (remainder_q >= 20):
        print(int(remainder_q / 10), 'Dimes')
    if remainder_q1 < 10 and (remainder_q1 >= 5):
        print(int(remainder_q1 / 5), 'Nickel')
    if remainder_q2 < 2 and (remainder_q2 == 1):
        print(int(remainder_q2 / 1), 'Penny')
    if remainder_q2 <= 4 and (remainder_q2 >= 2):
        print(int(remainder_q2 / 1), 'Pennies')
elif change <= 19 and (change >= 10):
    print(int(change / 10), 'Dime')
    if remainder_d < 10 and (remainder_d >= 5):
        print(int(remainder_d / 5), 'Nickel')
    if remainder_d1 < 2 and (remainder_d1 == 1):
        print(int(remainder_q2 / 1), 'Penny')
    if remainder_d1 <= 4 and (remainder_d1 >= 2):
        print(int(remainder_q2 / 1), 'Pennies')
elif change <= 24 and (change >= 20):
    print(int(change / 10), 'Dimes')
    if remainder_d < 10 and (remainder_d >= 5):
        print(int(remainder_d / 5), 'Nickel')
    if remainder_d1 < 2 and (remainder_d1 == 1):
        print(int(remainder_q2 / 1), 'Penny')
    if remainder_d1 <= 4 and (remainder_d1 >= 2):
        print(int(remainder_q2 / 1), 'Pennies')
elif change < 10 and (change >= 5):
    print(int(change / 5), 'Nickel')
    if remainder_n < 2 and (remainder_n == 1):
        print(int(remainder_q2 / 1), 'Penny')
    if remainder_n <= 4 and (remainder_n >= 2):
        print(int(remainder_q2 / 1), 'Pennies')
elif change < 2 and (change == 1):
    print(int(change / 1), 'Penny')
elif change <= 4 and (change >= 2):
    print(int(change / 1), 'Pennies')
else:
    print('No change')