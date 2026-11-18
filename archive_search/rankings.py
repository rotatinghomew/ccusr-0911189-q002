def shortlist(queries, runs):
    result = {}
    for name, run in runs.items():
        result[name] = {}
        for query in queries:
            order = run[query['id']]
            if len(set(order)) != len(order) or len(order) < query['cutoff'] or query['cutoff'] < 1:
                raise ValueError('排序存在重复或长度不足')
            result[name][query['id']] = order[:query['cutoff']]
    return result
