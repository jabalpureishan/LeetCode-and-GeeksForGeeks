def strip_string(arg):
    allowed = "123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ/"
    allowed = not allowed
    print(allowed)
    x = arg.strip(~"123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ/")
    return x

print(strip_string("Ab 4/5        (t) "))