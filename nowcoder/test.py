

def findMinPossibleNumber (allSum, A):
    if allSum < 0:
        return 0
    if A <= 0:
        return 0
    if allSum == A:
        return 1

    max_count = allSum // A
    for count in range(1, max_count + 1):
        if (allSum - count * A) % 10 == 0:
            return count

    return -1

if __name__ == '__main__':
    print(findMinPossibleNumber(10258, 9))