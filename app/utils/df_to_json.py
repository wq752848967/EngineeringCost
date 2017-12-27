from df_json import DFJson


def load_csv_into_DFJson(data):

    total = data.count()
    num = 50
    dd = data.limit(num).collect()
    head = dd[0].asDict().keys()
    body = [r.asDict().values() for r in dd[:]]
    num = min(total, num)
    return DFJson(head, body, total, num)