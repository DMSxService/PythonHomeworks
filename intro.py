def introspection_info(obj):
    result = {}
    tp = type(obj)
    result['type'] = tp.__name__
    attributes = []
    methods = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if isinstance(attr, int):
            attributes.append(attr_name)
            continue
        elif attr_name == '__doc__' or attr_name == '__class__':
            continue
        methods.append(attr_name)
    result['attributes'] = attributes
    result['methods'] = methods
    result['module'] = __name__
    return result


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)
