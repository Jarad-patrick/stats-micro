from typing import Iterable, List
from collections import Counter

def mean(data: Iterable[float]) -> float:
    data_list = list(data)
    if not data_list:
        raise ValueError("mean requires at least one data point")
    return sum(data_list) / len(data_list)

def median(data: Iterable[float]) -> float:
    data_list = sorted(list(data))
    n = len(data_list)
    if n == 0:
        raise ValueError("median requires at least one data point")
    mid = n // 2
    if n % 2 == 1:
        return float(data_list[mid])
    else:
        return (data_list[mid - 1] + data_list[mid]) / 2.0

def mode(data: Iterable[float]) -> List[float]:
    data_list = list(data)
    if not data_list:
        raise ValueError("mode requires at least one data point")
    counts = Counter(data_list)
    max_count = max(counts.values())
    modes = [val for val, cnt in counts.items() if cnt == max_count]
    return sorted(modes)



def variance(data: Iterable[float]) -> float:
    data_list = list(data)
    if len(data_list) < 2:
        raise ValueError("variance requires at least two data points")
    
    m = mean(data_list)
    return sum((x - m) ** 2 for x in data_list) / (len(data_list) - 1)  # sample variance


def standard_deviation(data: Iterable[float]) -> float:
    return variance(data) ** 0.5
