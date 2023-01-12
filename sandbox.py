def print_them_all_v4(a, b=5, *args, **kwargs):
    print("PTAV4")
    print("a&b", a, b)
    print("тип args:", type(args))
    print(args)
    for i, argument in enumerate(args):
        print("позиционный параметр:", i, argument)
    print("тип kwargs:", type(kwargs))
    print(kwargs)
    for klyuch, znachenie in kwargs.items():
        print("именованный аргумент", klyuch, "=", znachenie)

print_them_all_v4(5, cat='мяу!', address='Moscow')