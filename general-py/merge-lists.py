def merge(list1: list, list2:list)->list:
    result = []
    i, j= 0,0
    while i<len(list1) and j<len(list2):
        if list1[i]<=list2[j]:
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1

    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

merged_list = merge([100, 150, 200], [125, 175])        
print(merged_list)