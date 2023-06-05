# 实现迪杰斯特拉算法
import numpy as np

def startwith(start: int, mgraph: np.ndarray) -> list:
    """
    :param start: 出发点的索引，从0开始
    :param mgraph: 设置好的邻接矩阵，二维numpy数组
    :return: 一个列表，各元素值是从start到对应下标的点的最短距离
    """
    # 定义一个遍历过得点集合和未遍历过的点集合
    passed = [start]
    nopassed = [i for i in range(len(mgraph)) if i != start]
    distance = mgraph[start]
    while nopassed:
        min_id = nopassed[0]
        for i in nopassed:
            if distance[i] < distance[min_id]:
                min_id = i
        nopassed.remove(min_id)
        passed.append(min_id)
        for i in nopassed:
            if distance[min_id] + mgraph[min_id][i] < distance[i]:
                distance[i] = distance[min_id] + mgraph[min_id][i]
    return distance

