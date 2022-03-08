def stylish(value):
    if value is None:
        return 'null'

    if isinstance(value, str):
        return f"'{value}'"

    if not isinstance(value, dict):
        return str(value).lower()

    return '[complex value]'
