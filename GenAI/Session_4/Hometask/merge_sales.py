def merge_sales_dictionaries(dict1, dict2):
    merged_dict = {}
    for key, value in dict1.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    return merged_dict
    
sales1 = {"apple": 10, "banana": 5, "orange": 15}
sales2 = {"banana": 3, "grape": 7, "apple": 2}

merged_sales = merge_sales_dictionaries(sales1, sales2)
print(merged_sales)