def get_num(prompt):  # funk dlya proverki vvoda
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Это не число")
            continue
        else:
            break
    return value
