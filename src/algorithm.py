import random
import math

def inputArray() :
    dimension = int(input("Masukkan jumlah dimensi ruang dari titik: "))
    while (dimension <= 2) :
        print("Masukkan salah. Silakan input lagi!")
        dimension = int(input("Masukkan jumlah dimensi ruang dari titik: "))
    
    vertex = int(input("Masukkan jumlah titik yang ingin dibentuk: "))
    while (vertex <= 1) :
        print("Masukkan salah. Silakan input lagi!")
        vertex = int(input("Masukkan jumlah titik yang ingin dibentuk: "))

    array = [[0 for x in range(dimension)] for y in range(vertex)]
    for i in range(vertex) :
        for j in range(dimension) :
            array[i][j] = round(random.uniform(0,100),2)
    return array

def printArray(array) :
    for i in range(len(array)) :
        for j in range(len(array[0])) :
            print(str(array[i][j]), end = " ")
        print("")

def divide(array) :
    S1 = []
    S2 = []
    for i in range(len(array)) :
        if (i < len(array)//2) :
            S1.append(array[i])
        else :
            S2.append(array[i])
    return S1, S2

def euclideanDistance(array1, array2, n) :
    sum = 0
    for i in range(len(array1)) :
        sum += (array1[i] - array2[i])**2
    distance = math.sqrt(sum)
    array = [array1,array2]
    n += 1
    return distance, array, n    

def min(d1, d2) :
    if (d1 < d2) :
        return d1
    else :
        return d2

def findClosestPair(array, n) :
    if (len(array) == 2) :
        dist, closestArray, n = euclideanDistance(array[0], array[1], n)
    elif (len(array) == 3) :
        dist1, closestArray1, n = euclideanDistance(array[0], array[1], n)
        dist2, closestArray2, n = euclideanDistance(array[0], array[2], n)
        dist3, closestArray3, n = euclideanDistance(array[1], array[2], n)
        dist = min(min(dist1,dist2),dist3)
        if (dist == dist1) :
            closestArray = closestArray1
        else :
            if (dist == dist2) :
                closestArray = closestArray2
            else :
                closestArray = closestArray3  
    else :
        S1, S2 = divide(array)
        d1, closestA1, n = findClosestPair(S1, n)
        d2, closestA2, n = findClosestPair(S2, n)
        dist = min(d1, d2)
        if (dist == d1) :
            closestArray = closestA1
        else :
            if (dist == d2) :
                closestArray = closestA2
        dist, closestArray = sStrip(dist, closestArray, array, n)
    return dist, closestArray, n

def sStrip(d, closestA, array, n) :
    if (len(array) % 2 == 1) :
        x = array[len(array)//2+1][0]
    else :
        x = (array[len(array)//2][0] + array[len(array)//2+1][0])/2
    S = []
    for i in range(len(array)) :
        if (array[i][0] >= x-d and array[i][0] <= x+d) :
            S.append(array[i])
    for i in range(len(S)) :
        for j in range(i+1,len(S)) :
            dist, a, n = euclideanDistance(S[i],S[j], n)
            if (dist < d) :
                d = dist
                closestA = a
    return d, closestA

def bruteForce(array):
    n = 0
    d, A, n = euclideanDistance(array[0],array[1], n)
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j :
                d1, a, n = euclideanDistance(array[i],array[j], n)
                if d1 <= d:
                    d = d1
                    A = a
    return d, A