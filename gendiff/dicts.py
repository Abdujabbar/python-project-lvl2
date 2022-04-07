from collections import defaultdict


def build_dicts_diff_for_key(d1, d2, key):
    if key not in d1:
        return {
            'action': 'record_added',
            'value': d2.get(key)
        }

    if key not in d2:
        return {
            'action': 'record_deleted',
            'value': d1.get(key)
        }

    if isinstance(d1[key], dict) and isinstance(d2[key], dict):
        return {
            'action': 'record_nested',
            'children': build_difference(d1[key], d2[key])
        }

    if d1.get(key) != d2.get(key):
        return {
            'action': 'record_changed',
            'old': d1.get(key),
            'new': d2.get(key)
        }

    return {
        'action': 'record_same',
        'value': d1.get(key)
    }


def build_difference(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise Exception("Unexpected parametr, function awaits dicts only")

    all_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    dicts_diff = defaultdict(tuple)
    for key in all_keys:
        dicts_diff[key] = build_dicts_diff_for_key(dict1, dict2, key)

    return dicts_diff
