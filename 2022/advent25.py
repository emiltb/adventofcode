data = [f for f in open("inputs/input25.txt").read().splitlines()]


def snafu_to_num(num):
    ret_num = 0
    for i, s in enumerate(num[::-1]):
        if s == "-":
            ret_num += (-1) * 5**i
        elif s == "=":
            ret_num += (-2) * 5**i
        else:
            ret_num += int(s) * 5**i
    return ret_num


total = 0
for l in data:
    total += snafu_to_num(l)

snafu_total = ""


def num_to_snafu(num):
    snafu_num = ""

    while num:
        # Check last digit
        remains = num % 5
        # Remove a power of 5
        num = num // 5

        # If last digit is 0-2, then just use that
        if remains <= 2:
            snafu_num = str(remains) + snafu_num
        # Otherwise convert to the corresponding = or -
        else:
            snafu_num = "   =-"[remains] + snafu_num
            num += 1

    return snafu_num


print(num_to_snafu(total))
