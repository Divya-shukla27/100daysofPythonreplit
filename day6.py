print("MY LOGIN SYSTEM")
print("+++++++++++++++")
n = input("Username > ")
p = input("Password > ")
if (n == "mark" and p == "password"):
    print("welcome mark")
elif (n == "mark" or p == "password"):
    print("check your username and password again")
else:
    print("invalid login")
