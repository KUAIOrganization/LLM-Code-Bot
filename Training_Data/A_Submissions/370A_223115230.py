def main():
    r1, c1,r2,c2 = map(int, input().split())
    # r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print("0 0 0")
        return

    # rook
    if r1 == r2 or c1 == c2:
        print("1 ", end="")
    else:
        print("2 ", end="")

    # bishop
    if (r1 + c1) % 2 != (r2 + c2) % 2:
        print("0 ", end="")
    elif abs(r1 - r2) == abs(c1 - c2):
        print("1 ", end="")
    else:
        print("2 ", end="")

    # king
    print(max(abs(r1 - r2), abs(c1 - c2)))


if __name__ == "__main__":
    main()
