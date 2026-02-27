global_counter = 0
result_value = 0

def outer_function():
    nonlocal_counter = 0

    def inner_function():
        nonlocal nonlocal_counter
        global global_counter

        for _ in range(int(input())):
            command, value = input().split()
            value = int(value)

            if command == "global":
                global_counter += value
            elif command == "nonlocal":
                nonlocal_counter += value

        return nonlocal_counter

    return inner_function()

result_value = outer_function()
print(global_counter, result_value)