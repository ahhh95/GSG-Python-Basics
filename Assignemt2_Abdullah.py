Math = float(input("Enter your Math mark: "))
if Math >= 50:
    print("You Passed Math Course")
else:
    print("You Failed Math Course")

Science = float(input("Enter your Science mark: "))
if Science >= 50:
    print("You Passed Science Course")
else:
    print("You Failed Science Course")

History = float(input("Enter your History mark: "))
if History >= 50:
    print("You Passed History Course")
else:
    print("You Failed History Course")

Geography = float(input("Enter your Geography mark: "))
if Geography >= 50:
    print("You Passed Geography Course")
else:
    print("You Failed Geography Course")

English = float(input("Enter your English mark: "))
if English >= 50:
    print("You Passed English Course")
else:
    print("You Failed English Course")

Average = (Math + Science + History + Geography + English) / 5
print(f"Your Final Average is {Average}")

if Average >= 85:
    print("You are Excellent")
if 85 > Average >= 75:
    print("You are Very Good")
if 75 > Average >= 65:
    print("You are Good")
if 65 > Average >= 50:
    print("Pass")
if Average < 50:
    print("Fail")

if (Average >= 85 and Math >= 80) or (Average < 85 and Math >= 90):
    print("You can join the competition!")
else:
    print("You can NOT join the competition!!")