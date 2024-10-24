def binary_search(nums, target, low, hi):
    while low < hi:
        mid = (low + hi) // 2 
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1  
        else:
            low = mid + 1 
    return -1
            
def exponential_search(arr, target):
    if arr[0] == target:
        return 0 
    
    l, r = 1, len(arr)
    
    while l < r and arr[l] < target:
        l *= 2
        
        if l >= len(arr):  
            break

        if arr[l] == target:
            return l
        
    return binary_search(arr, target, l//2, min(l, r - 1))

def test_exponential_search():
    # Caso 1: Elemento presente no início
    arr1 = [1, 2, 3, 4, 5]
    target1 = 1
    result1 = exponential_search(arr1, target1)
    print(f'Teste 1 - Esperado: 0, Obtido: {result1}')

    # Caso 2: Elemento presente no final
    arr2 = [1, 2, 3, 4, 5]
    target2 = 5
    result2 = exponential_search(arr2, target2)
    print(f'Teste 2 - Esperado: 4, Obtido: {result2}')

    # Caso 3: Elemento não presente (menor que o menor)
    arr3 = [1, 2, 3, 4, 5]
    target3 = 0
    result3 = exponential_search(arr3, target3)
    print(f'Teste 3 - Esperado: -1, Obtido: {result3}')

    # Caso 4: Elemento não presente (maior que o maior)
    arr4 = [1, 2, 3, 4, 5]
    target4 = 6
    result4 = exponential_search(arr4, target4)
    print(f'Teste 4 - Esperado: -1, Obtido: {result4}')
    
    # Caso 5: Elemento presente no meio
    arr5= [1, 2, 3, 4, 5]
    target5 = 3
    result5 = exponential_search(arr5, target5)
    print(f'Teste 5 - Esperado: 2, Obtido: {result5}')

# Chama a função de teste
test_exponential_search()