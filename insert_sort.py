def insert_sort(array, n):
    for i in range(1, n):
        x = array[i] # 'wyciągnięcie' elme
        j = i-1
        while j >= 0 and array[j] > x: # szukamy miejsca do wstawienia elementu
            array[j+1] = array[j]
            j -= 1
        array[j+1] = x # wstawienie elementu x
    print(array)

array = [3, 1, 2, 4, 0]
insert_sort(array, len(array))