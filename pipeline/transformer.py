
def is_active(r):
    """True if this record has revenue and at least one item."""
    return r.revenue > 0 and r.item_count > 0


def get_active(records):
    """Keep only records that have revenue and at least one item."""
    return list(filter(is_active, records))


def get_net_margins(records, cost_ratio=0.6):
    """Net margin for each record = revenue minus 60% costs."""
    return [r.revenue * (1 - cost_ratio) for r in records]


