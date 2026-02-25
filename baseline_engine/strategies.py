RPC_LIST = ["cloudflare", "publicnode", "llamarpc"]

rr_index = 0


def single_rpc(rows):
    """
    Always choose the same RPC.
    """
    return "publicnode"


def round_robin(rows):
    """
    Rotate between RPC providers.
    """
    global rr_index

    rpc = RPC_LIST[rr_index]
    rr_index = (rr_index + 1) % len(RPC_LIST)

    return rpc


def lowest_latency(rows):
    """
    Choose RPC with the lowest latency.
    """
    best = rows.loc[rows["latency_ms"].idxmin()]
    return best["rpc_id"]


def freshest_block(rows):
    """
    Choose RPC with smallest block lag.
    """
    best = rows.loc[rows["block_lag"].idxmin()]
    return best["rpc_id"]