def desk(pending):
    return [row['ticket'] for row in sorted(pending, key=lambda row: (-row['priority'], row['ticket']))
            if row['state'] == 'open']
