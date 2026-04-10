def set_operations(set1, set2):
    return {
        "union": set1.union(set2),
        "intersection": set1.intersection(set2),
        "difference": set1.difference(set2),
        "symmetric_difference": set1.symmetric_difference(set2)
    }