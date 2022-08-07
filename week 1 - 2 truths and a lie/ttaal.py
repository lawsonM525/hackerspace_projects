statements = []
lie_index = 99

for i in range(3):
    statements.append(str(i+1)+". "+str(input("What is your statement #"+str(i+1)+"?")))
    answer=input("Is this the lie? answer yes/no")
    if answer == "yes":
        lie_index=i+1
        print("Noted it's #"+str(lie_index)) #for confirmation

print("Good. You can let the player play now.")

print("Hello player. Below are three statements.")
for line in statements:
    print(line)

print(lie_index)
user_answer = input("Which of the above is a lie? (1,2 or 3)")
print(user_answer)
if user_answer == lie_index:
    print("Well done! You're right!")
else:
    print("Nope. Start again with some new statements")

