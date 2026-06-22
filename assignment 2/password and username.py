#validating username and password 
def validate_credentials(username, password):
    result = {"username":[], "password":[]}

    # checks for username
    if len(username) < 6:
        result["username"].append("Must be at least 6 characters")

    if " " in username:
        result["username"].append("Must not contain spaces")

    if not username[0].isalpha():
        result["username"].append("Must start with a letter")
    
    # counters
    upper = 0
    lower = 0
    digit = 0
    special = 0

    #looping through the password
    for char in password:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        else:
            special += 1

    # checks for password 
    if len(password) < 8:
        result["password"].append("Must be at least 8 characters")

        if upper == 0:
            result["password"].append("Uppercase needed")
        if lower == 0:
            result["password"].append("Lowercase needed")
        if digit == 0:
            result["password"].append("Number needed")
        if special == 0:
            result["password"].append("Special character needed")

    return result

# suggestions for weak password
def generate_suggestions(password):
    sugg = [] 
    if len(password) < 8:
        sugg.append("Make it longer")
    if password.islower():
        sugg.append("Add uppercase")
    if password.isupper():
        sugg.append("Add lowercase")
    if password.isalpha():
        sugg.append("Add number")
    if password.isalnum():
        sugg.append("Add a special character")

    return sugg

 # Tests

tests = [
    ("Bright11", "Python@44"),
    ("mekus", "fgooju"),
    ("456function", "class456#"),
    ("panda22", "specter"),
    ("ema cul22", "assure%33"),
    ("adaobi", "random&33")]

for username, password in tests:
    print("\nConnecting:", username, password)
    result = validate_credentials(username, password)
    print(result)

    # Always show suggestions, even if password is strong
    suggestions = generate_suggestions(password)
    if suggestions:
        print("suggestions:", suggestions)
    else:
        print("suggestions: You are logged in!")
