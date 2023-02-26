import time
from algorithm import *
from visualize import *

def main() :
    arrayV = inputArray()
    print("S : ")
    printArray(arrayV)
    arrayV.sort(key=lambda vertex: vertex[0])
    n = 0
    startTimeDnC = time.time()
    distDnC, closestArrayDnC, n = findClosestPair(arrayV, n)
    finishTimeDnC = time.time()
    startTimeBF = time.time()
    distBF, closestArrayBF = bruteForce(arrayV)
    finishTimeBF = time.time()
    print("\nALGORITMA DIVIDE AND CONQUER")
    print("Jarak titik terdekat                          :", (distDnC))
    print("Pasangan titik terdekat                       :")
    printArray(closestArrayDnC)
    print("Execute Time                                  :", (finishTimeDnC-startTimeDnC), "s")
    print("Banyaknya operasi perhitungan rumus Euclidean :", n)
    print("______________________________________________________________________________________________")
    print("ALGORITMA BRUTE FORCE")
    print("Jarak titik terdekat                          :", (distBF))
    print("Pasangan titik terdekat                       :")
    printArray(closestArrayBF)
    print("Execute Time                                  :", (finishTimeBF-startTimeBF), "s")
    if (len(arrayV[0]) == 3) :
        visualize(arrayV, closestArrayDnC)

if __name__ == "__main__":
    main()