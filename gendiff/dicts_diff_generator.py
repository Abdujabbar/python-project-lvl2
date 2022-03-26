from collections import defaultdict


def parse_node(d1, d2, key):
    if key not in d1:
        return {
            'action': 'record_added',
            'node': d2.get(key)
        }

    if key not in d2:
        return {
            'action': 'record_deleted',
            'node': d1.get(key)
        }

    if isinstance(d1[key], dict) and isinstance(d2[key], dict):
        return {
            'action': 'record_nested',
            'children': generate_dicts_difference(d1[key], d2[key])
        }

    if d1.get(key) != d2.get(key):
        return {
            'action': 'record_changed',
            'old': d1.get(key),
            'new': d2.get(key)
        }

    return {
        'action': 'record_same',
        'node': d1.get(key)
    }


def generate_dicts_difference(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        raise Exception("Unexpected parametr, function awaits dicts only")

    all_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    dicts_diff = defaultdict(tuple)
    for key in all_keys:
        dicts_diff[key] = parse_node(dict1, dict2, key)

    return dicts_diff
