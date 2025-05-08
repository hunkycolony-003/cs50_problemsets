def main():
    tests = int(input())
    for _ in range(tests):
         print(test_case())

def test_case():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    count = 0

    while True:
        if count not in a:
            for i in range(count - x, 0, -x):
                if a.count(i) > 1:
                    a.pop(i)
                    a.append(count)
                    break
            else:
                return count
        count += 1

if __name__ == "__main__":
     main()
