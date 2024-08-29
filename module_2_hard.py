def get_password(n):
    result = ""
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            sum_ij = i + j
            if n % sum_ij == 0:
                if result:
                    result += " "
                result += str(i) + str(j)
    return result
print(get_password(9))  # Output: 1 2 1 8 2 7 3 6 4 5
print(get_password(11))  # Output: 1 10 2 9 3 8 4 7 5 6