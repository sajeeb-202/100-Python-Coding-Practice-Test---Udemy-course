def get_indices_with_for_loop(list):
    if list == []:
        return []
    return_list = []
    for i in range(len(list)):
        return_list.append(i,list[i])
        return return_list 
        


print(get_indices_with_for_loop([5, 5, 5]))