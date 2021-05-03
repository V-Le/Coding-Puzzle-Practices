def valid_spacing(s):
    # write your code here
    if len(s) >= 1:
        if " " in s[-1] or " " in s[0] or "  " in s:
            return False
        else:
            return True
    else:
        return True

print(valid_spacing(""))
