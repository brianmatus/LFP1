def check(n):
    if n % 2 != 0:
        print("Weird")
        return
    if (n >= 2 and n <= 5):
        print("Not Weird")
        return
    if (n >= 6 and n <= 20):
        print("Weird")
        return
    if (n > 20):
        print("Not Weird")
        return
if __name__ == '__main__':
    n = int(input().strip())
    check(n)
