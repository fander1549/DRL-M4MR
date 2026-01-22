# -*- coding: utf-8 -*-
import os
class MiniConfig:
    # --- 基础路径配置 (Linux 环境建议使用绝对路径) ---
    # 你只需要在这里修改一次，其他路径会自动更新
    
    
    BASE_PATH = "/home/hs/DRL-M4MR" 

    # --- 拓扑文件路径 ---
 #  XML_TOPOLOGY_PATH = os.path.join(BASE_PATH, "mininet/topologies/topology2.xml")
 #   LINKS_INFO_PATH = os.path.join(BASE_PATH, "mininet/links_info/links_info.xml")

    # --- 流量矩阵 (TM) 相关路径 ---
    TM_SAVE_DIR = os.path.join(BASE_PATH, "mininet/tm_statistic")
    MEAN_TIME_TM_PATH = os.path.join(TM_SAVE_DIR, "mean_time_tm.npy")
    
    # iperf 脚本输出目录
    #IPERF_TM_DIR = os.path.join(BASE_PATH, "mininet/iperfTM")