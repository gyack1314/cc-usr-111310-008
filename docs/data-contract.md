# 分桶路由与迁移协议

环token为[0,2^token_bits)整数且唯一，按升序查首个>=key_token节点为owner，超过最大token回绕首节点；节点拥有(prev,token]，token恰端点归该节点。生产key_token用UTF8 key的SHA256前8字节大端模2^token_bits，材料token为显式受信任测试映射，不要求恰与hash一致，正式计算需可注入hash映射并记录其版本。

旧环40A/200B到新环40A/120C/200B，只有(40,120]从B移C。其他范围包括(200,40]回绕仍A。另一资料增加10C会迁移(200,10]回绕区间。一个owner可有多个虚拟节点，差分按完整区间及owner比较合并，不以节点数量猜。

base_position为冻结旧owner在该区间的一致状态；source_log按提交位置追赶，包括删除，cutover_position声明短事务锁定的完整末位置，日志须覆盖到它，不缺就绪证明。切换后新owner分配大于该区间旧token的fence，旧reader固定原路由及原数据版本只读，旧writer拒绝。按逻辑步骤提供冻结末尾与写入调度，不使用真实等待。初始工具只检查环token及源操作，不路由。
