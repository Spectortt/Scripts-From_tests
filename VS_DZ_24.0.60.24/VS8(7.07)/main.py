# def count_char_frequency(text):
#     frequency_dict = {}
#     for char in text:
#         if char in frequency_dict:
#             frequency_dict[char] += 1
#         else:
#             frequency_dict[char] = 1
#     return frequency_dict
# #----------------------------------------------------------------------

# def merge_dicts(dict1, dict2):
#     merged_dict = {}
#     for key in set(list(dict1.keys()) + list(dict2.keys())):
#         if key in dict1 and key in dict2:
#             merged_dict[key] = [dict1[key], dict2[key]]
#         elif key in dict1:
#             merged_dict[key] = dict1[key]
#         else:
#             merged_dict[key] = dict2[key]
#     return merged_dict
# #----------------------------------------------------------------------

# def invert_dict(unique_dict):
#     inverted_dict = {}
#     for key, value in unique_dict.items():
#         inverted_dict[value] = key
#     return inverted_dict
# #----------------------------------------------------------------------

# def sort_dict_by_keys(dict, reverse=False):
#     sorted_dict = {}
#     for key in sorted(dict.keys(), reverse=reverse):
#         sorted_dict[key] = dict[key]
#     return sorted_dict
# #----------------------------------------------------------------------

# def find_keys_by_value(dict, value):
#     matching_keys = []
#     for key, val in dict.items():
#         if value in str(val):
#             matching_keys.append(key)
#     return matching_keys
# #----------------------------------------------------------------------

# def list_of_tuples_to_dict(list_of_tuples):
#     dict = {}
#     for tuple in list_of_tuples:
#         dict[tuple[0]] = tuple[1]
#     return dict
# #----------------------------------------------------------------------

# def group_list_by_values(list_of_tuples):
#     grouped_dict = {}
#     for tuple in list_of_tuples:
#         if tuple[0] in grouped_dict:
#             grouped_dict[tuple[0]].append(tuple[1])
#         else:
#             grouped_dict[tuple[0]] = [tuple[1]]
#     return grouped_dict
# #----------------------------------------------------------------------

# def merge_lists_by_key(dict1, dict2):
#     merged_dict = {}
#     for key in set(list(dict1.keys()) + list(dict2.keys())):
#         if key in dict1 and key in dict2:
#             merged_dict[key] = dict1[key] + dict2[key]
#         elif key in dict1:
#             merged_dict[key] = dict1[key]
#         else:
#             merged_dict[key] = dict2[key]
#     return merged_dict
# #----------------------------------------------------------------------

# def find_max_min_values(dict):
#     max_key = max(dict, key=dict.get)
#     min_key = min(dict, key=dict.get)
#     return max_key, min_key
# #----------------------------------------------------------------------
# def sum_nested_dict_values(nested_dict):
#     total_sum = 0
#     for value in nested_dict.values():
#         if isinstance(value, dict):
#             total_sum += sum_nested_dict_values(value)
#         else:
#             total_sum += value
#     return total_sum