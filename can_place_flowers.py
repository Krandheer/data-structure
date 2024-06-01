def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return True
    for i in range(len(flowerbed) - 1):
        if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            n -= 1
            flowerbed[i] = 1
            if n == 0:
                return True
        elif (
            i != len(flowerbed) - 1
            and flowerbed[i - 1] == 0
            and flowerbed[i + 1] == 0
            and flowerbed[i] == 0
        ):
            n -= 1
            flowerbed[i] = 1
            if n == 0:
                return True
        if i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
            n -= 1
            flowerbed[i] = 1
            if n == 0:
                return True
    if n != 0:
        if flowerbed[-2] == 0 and flowerbed[-1] == 0:
            n -= 1
    return n == 0


flower = [1, 0, 0, 0, 1, 0, 0]
n = 1

ans = canPlaceFlowers(flower, 2)
print(ans)
