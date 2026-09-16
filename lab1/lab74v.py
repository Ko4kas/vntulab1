for _ in range(3):
        n =int(input("Введіть n: "))
        power = n ** 10
        repeated_text = str(power) * 4
        repeated_number = int(repeated_text)
        result = repeated_number ** (1 / 10)
        print(result)