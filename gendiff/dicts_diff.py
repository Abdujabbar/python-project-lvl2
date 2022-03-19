from collections import defaultdict


def detect_method_for_item(d1, d2, key):
    if key not in d1:
        return {
            'method': 'record_added',
            'item': [d2.get(key)]
        }

    if key not in d2:
        return {
            'method': 'record_deleted',
            'item': [d1.get(key)]
        }

    if isinstance(d1[key], dict) and isinstance(d2[key], dict):
        return {
            'method': 'record_nested',
            'item': [dicts_diff(d1[key], d2[key])]
        }

    if d1.get(key) != d2.get(key):
        return {
            'method': 'record_changed',
            'item': [d1.get(key), d2.get(key)]
        }

    return {
        'method': 'record_same',
        'item': [d1.get(key)]
    }


def dicts_diff(dict1, dict2):
    all_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    dicts_diff = defaultdict(tuple)
    for key in all_keys:
        dicts_diff[key] = detect_method_for_item(dict1, dict2, key)

    return dicts_diff
