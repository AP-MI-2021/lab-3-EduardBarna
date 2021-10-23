def citire_lista():
    l =[]
    givenString = input("Introduceti lista de numere intregi separate prin virgula: ")
    numbersAsString = givenString.split(',')
    for i in numbersAsString:
        l.append(int(i))
    return l


def is_palindrome(n):
    '''
    verifica daca un nr este prim
    :param n: numarul pe care il verificam sa fie palindrom
    :return: True, daca nur este palindrom si False daca nu este
    '''
    x=str(n)
    if x == x[::-1]:
        return True
    else:
        return False

def is_power_k(n, k):
    '''
    determina daca un nr n poate fi scris ca x^k unde x este un numar intreg pozitiv
    :param n: numarul caruia ii verificam radacina de ordin k
    :param k: puterea la care il ridicam pe x
    :return: True, daca poate fi scris ca un nr intreg x la puterea k si false daca nu
    '''

    if n ** (1/k) == int(n ** (1/k)):
        return True
    else:
        return False





def get_longest_all_palindromes(l):
    '''
    determina cea mai lunga subsecventa care contine palindroame
    :param l: lista initiala
    :return: subsecventa cea mai lunga care contine palindroame
    '''
    subsecventa_max=[]
    start = -1
    for i in range(len(l)):
        if is_palindrome(l[i]):
            if start == -1:  # daca  nu ne aflam intr-o subsecventa
                start = i  #incepem subseventa de la pozitia i
            if len(subsecventa_max) < i-start+1:  #daca lungimea subsecventei max este mai mica decat lungimea subsecventei curente
                subsecventa_max = l[start:i+1]
        else:
            start = -1
    return subsecventa_max


def get_longest_powers_of_k(l, k):
    '''

    :param l: lista de numere intregi
    :param k: ordinul radacinii pe care numerele trebuie sa o aiba
    :return: subsecventa cea mai lunga care are numere cu radacini de ordin k
    '''
    start = -1
    subsecventa_max = []
    for i in range(len(l)):
        if is_power_k(l[i], k):
            if start == -1:
                start = i
            if len(subsecventa_max) < i-start+1:
                subsecventa_max = l[start:i+1]
        else:
            start = -1
    return subsecventa_max

def get_longest_arithmetic_progression(l):
    '''
    Determina cea mai mare subsecventa de numere aflate intr-o progresie arirmetica
    :param l: lista initiala de numer intregi
    :return: cea mai mare subsecventa de numere aflate intr-o progresie arirmetica
    '''
    subsecventa_max = []
    start = -1
    for i in range(len(l)-2):
        if l[i+1] == (l[i] + l[i+2])/2:
            if start == -1:
                start = i
            if len(subsecventa_max) < i - start + 3:
                subsecventa_max = l[start:i+3]
        else:
            start = -1
    return subsecventa_max







def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(12561) == False
    assert is_palindrome(0) == True

def test_is_power_k():
    assert is_power_k(8, 3) == True
    assert is_power_k(27, 4) == False
    assert is_power_k(81,4) == True





def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([121, 787, 356, 6535, 232, 676, 898]) == [232, 676, 898]
    assert get_longest_all_palindromes([121]) == [121]
    assert get_longest_all_palindromes([1]) == [1]
    assert get_longest_all_palindromes([154]) == []

def test_get_longest_power_of_k():
    assert get_longest_powers_of_k([5, 25, 7, 36, 49, 16], 2) == [36, 49, 16]
    assert get_longest_powers_of_k([8, 27, 17, 18, 9, 4, 64], 5) == []
    assert get_longest_powers_of_k([16, 81, 17, 18, 9, 4, 64], 4) == [16, 81]

def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([2, 5, 4, 5, 65, 23, 8, 11, 14]) == [8, 11, 14]
    assert get_longest_arithmetic_progression([1, 2, 3, 4, 6, 9, 6, 4]) == [1, 2, 3, 4 ]
    assert get_longest_arithmetic_progression([219,21,0,45]) == []




def main():
    test_get_longest_all_palindromes()
    test_get_longest_power_of_k()
    test_is_palindrome()
    test_is_power_k()
    test_get_longest_arithmetic_progression()
    l=[]
    while True:
        print("""
1.Introduceti o lista de numere intregi separate prin virgula
2.Afisati cea mai mare subsecventa care contine palindroame
3.Afisati cea mai mare subsecventa care contine numere ce pot fi scrie ca x la puterea k, unde x este nr natural
4.Afisati ce mai mare subsecventa care contine numere ce fac parte dintr-o progresie aritmetica
a.Afisati lista introdusa
x.Iesire
        """)
        optiune = input()
        if optiune == '1':
            l = citire_lista()
        elif optiune == '2':
            print(get_longest_all_palindromes(l))
        elif optiune == '3':
            k=int(input("Introduceti radacina de ordin k pe care sa o aiba numerele din lista:  "))
            print(get_longest_powers_of_k(l, k))
        elif optiune == '4':
            print(get_longest_arithmetic_progression(l))
        elif optiune == 'a':
            print(l)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida, va rog reincercati ")

if __name__ == "__main__":
    main()
