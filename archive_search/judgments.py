def index(collection, decisions):
    result = {}
    for row in decisions:
        if row['collection'] != collection:
            continue
        key = row['query'], row['segment']
        if row['relevant'] not in (0, 1) or key in result and result[key] != row['relevant']:
            raise ValueError('相关性判断无效或互相冲突')
        result[key] = row['relevant']
    return result
