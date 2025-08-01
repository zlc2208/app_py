def numsystem_convert(number_input="0", sys_input=10, sys_output=2):
    if any(int(x) > sys_input - 1 or int(x) < 0 for x in str(number_input)):
        return "Invalid input"
    else:
        num_input = number_input
        decimal_input = 0
        for i in range(len(num_input)):
            decimal_input += int(num_input[i]) * (sys_input ** (len(num_input) - i - 1))
        print(f"decimal_input: {decimal_input}", end="\n")
        decimal = decimal_input
        num_output = {}
        i = 0
        print("processing:")
        while True:
            if decimal - sys_output**i > 0:
                i += 1
            else:
                if decimal % sys_output**i == 0:
                    num_output[i] = decimal // sys_output**i
                    print("1:", i, decimal, num_output)
                    break
                else:
                    num_output[i - 1] = decimal // sys_output ** (i - 1)
                    decimal -= num_output[i - 1] * sys_output ** (i - 1)
                    print("2:", i, decimal, num_output)
                    if decimal == 0:
                        break
                    i = 0
        number_output = []
        length = max(num_output.keys()) + 1
        for i in range(length):
            if length - 1 - i in num_output:
                number_output.append(num_output[length - 1 - i])
            else:
                number_output.append(0)
        decimal_output = 0
        for i in range(len(number_output)):
            decimal_output += number_output[i] * (
                sys_output ** (len(number_output) - i - 1)
            )
        print(f"decimal_output: {decimal_output}", end="\n")
        result = "".join(str(x) for x in number_output)
        return result


if __name__ == "__main__":
    number_input = input("Enter the number to convert(>0): ")
    sys_input = int(input("Enter the input number system (2-10): "))
    sys_output = int(input("Enter the output number system (2-10): "))
    result = numsystem_convert(number_input, sys_input, sys_output)
    print(f"Converted number: {result}")
    a = input("Press Enter to exit...")
