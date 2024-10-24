def binary_search(nums, target):
    low, hi = 0, len(nums)  # Corrige o valor inicial de hi
    
    while low < hi:
        mid = (low + hi) // 2  # Corrige o cálculo de mid
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1  # Ajusta o intervalo de busca corretamente
        else:
            low = mid + 1  # Ajusta o intervalo de busca corretamente
    return -1
            
teste1 = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)  # Aqui deve retornar -1
print(teste1)
