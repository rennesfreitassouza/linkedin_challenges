
# find prime factors. [https://www.linkedin.com/learning/python-code-challenges/find-prime-factors]
def findAllPrimeFactors(value=None):
    
    prime_factors_list = list()
    print(f"{value}", end= " ")
    i = 2
    while (i <= value):
        if value % i == 0:
            prime_factors_list.append(i)
            value = value / i
            continue
        i += 1
        
    print(f"prime_factors_list: {prime_factors_list}")

    return prime_factors_list

def main():
    value = input("Enter a value: ")
    findAllPrimeFactors(int(value))

if __name__ == '__main__': main()