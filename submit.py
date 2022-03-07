# HENNGE CHALLENGE SOLUTION
# submitted by: Eric Torres, eric_torres@live.com
def solve_line(num_integers, line_int):
    if num_integers == 0:
        return 0
    else:
        current_num = int(line_int[num_integers - 1])
        if current_num > 0:
            return current_num * current_num +\
                solve_line(num_integers - 1, line_int)
        return solve_line(num_integers - 1, line_int)


def recursive_split(s, sep=' '):
    if sep in s:
        pos = s.index(sep)
        found = s[:pos]
        remainder = recursive_split(s[pos + 1:])
        remainder.insert(0, found)
        return remainder
    else:
        return [s]


def solve(num_test_cases):
    if num_test_cases == 0:
        return ""
    else:
        num_integers = input()
        line_int = input()
        line_int = recursive_split(line_int)
        answer = solve_line(int(num_integers), line_int)

        if num_test_cases > 1:
            return str(answer) + "\n" + solve(num_test_cases - 1)
        else:
            return str(answer) + solve(num_test_cases - 1)


def main():
    num_test_cases = input()
    answer = solve(int(num_test_cases))
    print(answer)


if __name__ == "__main__":
    main()
