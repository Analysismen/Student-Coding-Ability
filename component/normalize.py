def min_max_normalize(dict_before):
    max_value = max(zip(dict_before.values(), dict_before.keys()))[0]
    min_value = min(zip(dict_before.values(), dict_before.keys()))[0]
    max_sub = max_value - min_value
    dict_after = {}
    for key, val in dict_before.items():
        val = 100*(val-min_value)/max_sub
        dict_after[key] = val
    return dict_after

