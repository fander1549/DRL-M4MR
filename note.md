### 代码解释
network_structure.py 里在交换机连接时下发了 table‑miss 流表（上送控制器）。
shortest_path_forwarding.py 里会根据路径/组播树下发 实际转发流表（具体在它的 PacketIn 处理和流表下发逻辑里）。

### 启动前需要处理的bug
```python

```

#### 项目执行顺序：
generate_matrices.py $\rightarrow$ 2. iperf_script.py $\rightarrow$ 3. Ryu 控制器 $\rightarrow$ 4. generate_nodes_topo.py $\rightarrow$ 5. 修改 config.py 路径 $\rightarrow$ 6. train.py $\rightarrow$ 7. test.py。
 1. 启动 Mininet，加载拓扑文件，启动控制器和交换机。
 2. 控制器连接交换机，交换机下发 table‑miss 流表。 
    ```bash
    ryu-manager shortest_path_forwarding.py network_structure.py network_monitor.py network_delay.py arp_handler.py
 3. 交换机收到数据包，触发 PacketIn 事件，控制器