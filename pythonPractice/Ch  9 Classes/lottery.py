from random import choice

lottery_values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E')

my_ticket = "09B4"
count = 0


# Create a lottery ticket with 4 values
# for ignored in range(4):
#     lottery_ticket = choice(lottery_values)
#     print(lottery_ticket)

# lottery_ticket = str(choice(lottery_values)) + str(choice(lottery_values)) + str(choice(lottery_values)) + str(choice(lottery_values))
# print(lottery_ticket)

# A loop that counts how many tickets were pulled until my ticket wins.
# active = True
# while active:
#     ticket_called = str(choice(lottery_values)) + str(choice(lottery_values)) + str(choice(lottery_values)) + str(choice(lottery_values))
#
#     if ticket_called == my_ticket:
#         count += 1
#         print(count)
#         active = False
#     else:
#         count += 1

def get_ticket():
    return str(choice(lottery_values)) + str(choice(lottery_values)) + str(choice(lottery_values)) + str(
        choice(lottery_values))


while get_ticket() != my_ticket:
    count += 1

count += 1
print(count)
