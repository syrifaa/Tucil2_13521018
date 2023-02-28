import time
import os
from splashScreen import *
from algorithm import *
from visualize import *

def main() :
    flag = False
    while (flag == False) :
        splashScreen()
        arrayV = inputArray()
        arrayV = sortingArray(arrayV)
        # print("\nS : ")
        # printArray(arrayV)
        n1 = 0
        startTimeDnC = time.time()
        distDnC, closestArrayDnC, n1 = findClosestPair(arrayV, n1)
        finishTimeDnC = time.time()
        startTimeBF = time.time()
        distBF, closestArrayBF, n2 = bruteForce(arrayV)
        finishTimeBF = time.time()
        print("\n           ALGORITMA DIVIDE AND CONQUER        ")
        print("Jarak titik terdekat                          :", (distDnC))
        print("Pasangan titik terdekat                       :")
        printArray(closestArrayDnC)
        print("Execute Time                                  :", (finishTimeDnC-startTimeDnC), "s")
        print("Banyaknya operasi perhitungan rumus Euclidean :", n1)
        print("______________________________________________________________________________________________")
        print("\n             ALGORITMA BRUTE FORCE             ")
        print("Jarak titik terdekat                          :", (distBF))
        print("Pasangan titik terdekat                       :")
        printArray(closestArrayBF)
        print("Execute Time                                  :", (finishTimeBF-startTimeBF), "s")
        print("Banyaknya operasi perhitungan rumus Euclidean :", n2)
        if ((len(arrayV[0]) == 3) or (len(arrayV[0]) == 2)) :
            visualize(arrayV, closestArrayDnC)
        choose = str(input("\nApakah anda ingin mencari closest pair lagi? (yay/nay) "))
        while ((choose != "yay") and (choose != "nay")) :
            print("Masukkan salah. Silakan input lagi!")
            choose = str(input("Apakah anda ingin mencari closest pair lagi? (yay/nay) "))
        if (choose == "yay") :
            os.system('cls')
        else :
            flag = True

if __name__ == "__main__":
    main()