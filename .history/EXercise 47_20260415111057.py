def get_indices_with_for_loop(list):
    if list == []:
        return []
    else:
        for i in range(len(list)):
            return [i,list[i]]
        


print(get_indices_with_for_loop([5, 5, 5]))