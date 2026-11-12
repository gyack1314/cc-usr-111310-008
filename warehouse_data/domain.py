"""核对原始配置及数量，不执行仓库变换。"""
from .io import integer
def summarize(v,root):
    integer(v['token_bits'],1)
    for name in ('old_ring','new_ring'):
        ts=[x['token'] for x in v[name]]
        if len(ts)!=len(set(ts)) or any(type(x) is not int or not 0<=x<2**v['token_bits'] for x in ts):raise ValueError('环token非法')
    return {'old_nodes':len(v['old_ring']),'new_nodes':len(v['new_ring']),'log_records':len(v['source_log'])}
