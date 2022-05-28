def isPrime(num):
    divisores = 0
    array = []
    count = 1

    while count <= num:
        if num % count == 0:
            array.append(count)
            divisores += 1
        count += 1

    if divisores == 2:
        print("Primo", array)
    else:
        print("Composto\n", array)

def main():
    repet = 0
    while repet == 0:
        num = input("Insira um número inteiro: ")
        isPrime(int(num))

main()