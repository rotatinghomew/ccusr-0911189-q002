from .judgments import index
from .rankings import shortlist
from .review import desk


def report(data):
    judgments = index(data['collection'], data['judgments'])
    lists = shortlist(data['queries'], data['runs'])
    coverage = {name: {query: {'judged': sum((query, item) in judgments for item in order), 'total': len(order)}
                      for query, order in run.items()} for name, run in lists.items()}
    return {'coverage': coverage, 'pending': desk(data['pending'])}
