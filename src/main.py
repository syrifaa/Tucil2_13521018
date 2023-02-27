import time
from algorithm import *
from visualize import *

def main() :
    arrayV = inputArray()
    # print("\nS : ")
    # printArray(arrayV)
    arrayV.sort(key=lambda vertex: vertex[0])
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
    print("___________________________________________________________________________________________")
    print("\n             ALGORITMA BRUTE FORCE             ")
    print("Jarak titik terdekat                          :", (distBF))
    print("Pasangan titik terdekat                       :")
    printArray(closestArrayBF)
    print("Execute Time                                  :", (finishTimeBF-startTimeBF), "s")
    print("Banyaknya operasi perhitungan rumus Euclidean :", n2)
    if (len(arrayV[0]) == 3) :
        visualize(arrayV, closestArrayDnC)

if __name__ == "__main__":
    main()