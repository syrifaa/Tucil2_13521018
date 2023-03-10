import random
import math

# Input Titik dengan Pembangkit Acak
def inputArray() :
    dimension = int(input("Masukkan jumlah dimensi ruang dari titik     : "))
    while (dimension <= 1) :
        print("Masukkan salah. Silakan input lagi!")
        dimension = int(input("Masukkan jumlah dimensi ruang dari titik     : "))
    
    vertex = int(input("Masukkan jumlah titik yang ingin dibentuk    : "))
    while (vertex <= 1) :
        print("Masukkan salah. Silakan input lagi!")
        vertex = int(input("Masukkan jumlah titik yang ingin dibentuk    : "))

    array = [[0 for x in range(dimension)] for y in range(vertex)]
    for i in range(vertex) :
        for j in range(dimension) :
            array[i][j] = round(random.uniform(-100,100),2)
    return array

# Print Titik
def printArray(array) :
    for i in range(len(array)) :
        for j in range(len(array[0])) :
            print(str(array[i][j]), end = " ")
        print("")

# Sorting dengan Bubble Sort
def sortingArray(array) :
    for i in range(len(array)) :
        for j in range(0, len(array)-i-1) :
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Membagi Titik menjadi 2 Himpunan (Kiri(S1) dan Kanan(S2))
def divide(array) :
    S1 = []
    S2 = []
    for i in range(len(array)) :
        if (i < len(array)//2) :
            S1.append(array[i])
        else :
            S2.append(array[i])
    return S1, S2

# Menghitung Euclidean Distance
def euclideanDistance(array1, array2, n) :
    sum = 0
    for i in range(len(array1)) :
        sum += (array1[i] - array2[i])**2
    distance = math.sqrt(sum)
    array = [array1,array2]
    n += 1
    return distance, array, n    

# Mencari Minimum
def min(d1, d2) :
    if (d1 < d2) :
        return d1
    else :
        return d2

# Mencari Pasangan Titik Terdekat
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
        dist, closestArray, n = sStrip(dist, closestArray, array, n)
    return dist, closestArray, n

# Mencari Titik Terdekat dalam Sstrip
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
    return d, closestA, n

# Algoritma Brute Force
def bruteForce(array):
    d, A, n = euclideanDistance(array[0],array[1], -1)
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            d1, a, n = euclideanDistance(array[i],array[j], n)
            if d1 <= d:
                d = d1
                A = a
    return d, A, n