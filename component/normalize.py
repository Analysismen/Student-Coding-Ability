def min_max_normalize(dict_before):
    max_value = max(dict_before.values())
    min_value = min(dict_before.values())
    max_sub = max_value - min_value
    dict_after = {}
    for key, val in dict_before.items():
        if max_sub != 0:
            val = round(100 * (val - min_value) / max_sub, 2)
        dict_after[key] = val
    return dict_after
