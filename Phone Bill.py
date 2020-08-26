import math


def get_duration_in_sec(duration: str):
    tokens = duration.split(":")
    seconds = int(tokens[0]) * 60 * 60 + int(tokens[1]) * 60 + int(tokens[2])
    return seconds


def get_cost(call_sec: int):
    five_mins = 5 * 60
    one_min = 60
    if call_sec < five_mins:
        return call_sec * 3
    else:
        total_mins = math.ceil(call_sec / one_min)
        return total_mins * 150


def find_phone_num(search_num, phone_calls):
    return search_num in phone_calls


def cost_longest_duration(phone_calls):
    max_val = max(phone_calls.values(), key=lambda x: x[0])
    return max_val[1]


def solution(S: str):
    lines = S.split("\n")
    # phone_calls : {phone_number : (duration, cost)}
    phone_calls, total_cost = dict(), 0

    for i in range(len(lines)):
        tokens = lines[i].split(",")

        duration = tokens[0].strip()
        cost = get_cost(get_duration_in_sec(duration))

        phone_num = tokens[1].strip()
        repeated_phone_num = find_phone_num(phone_num, phone_calls)
        if not repeated_phone_num:
            phone_calls[phone_num] = [get_duration_in_sec(duration), cost]
        else:
            (phone_calls[phone_num])[1] += cost
            (phone_calls[phone_num])[0] += get_duration_in_sec(duration)

        total_cost += cost

    print(phone_calls)
    print("Total w/o deduction: ", total_cost)

    # Taking off the contribution of longest call
    cost_longest = cost_longest_duration(phone_calls)
    print("Cost of longest  ", cost_longest)
    total_cost -= cost_longest
    return total_cost


if __name__ == '__main__':
    log = "00:01:07,400-234-090 \n 00:05:01,701-080-080 \n 00:05:00,400-234-090"
    log2 = "00:01:07,400-234-090 \n 00:05:01,701-080-080 \n 00:05:01,701-000-080"
    print(solution(log2))


