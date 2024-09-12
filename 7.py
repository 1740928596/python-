def main():
    N = int(input().strip())
    result=[]
    for _ in range(N):
        x, y, t = map(int, input().strip().split())
        str_input = input().strip()

        if x == 0 and y == 0:  # Special case
            print(0)
            continue

        # Determine characters to count in x and y directions
        if x >= 0:
            X = 'R'
        else:
            X = 'L'
            x = -x

        if y >= 0:
            Y = 'U'
        else:
            Y = 'D'
            y = -y

        res = -1
        for i in range(t):
            if str_input[i] == X:
                x -= 1
            elif str_input[i] == Y:
                y -= 1

            if x <= 0 and y <= 0:
                res = i + 1
                break

        result.append(res)
    for i in result:
        print(i)

if __name__ == "__main__":
    main()
