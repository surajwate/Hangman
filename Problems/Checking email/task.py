def check_email(string):
    flag = True
    if " " in string:
        flag = False
    elif "@" not in string:
        flag = False
    elif (string.rfind(".") - string.rfind("@")) < 2:
        flag = False
    else:
        flag = True
    return flag
