def matcher(arg:str):
    match arg:
        case "username":
            return "Username"
        case "password":
            return "Password"
        case _:
            return "Invalid"
        
match = matcher("userame")
print(match)