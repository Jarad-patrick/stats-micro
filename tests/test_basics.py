from stats_pkg.basics import mean, median, mode, variance, standard_deviation

def test_mean():
    assert mean([1, 2, 3]) == 2

def test_median():
    assert median([3, 1, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5

def test_mode():
    assert mode([1, 1, 2, 2]) == [1, 2]
    assert mode([3, 3, 3, 1]) == [3]

def test_variance():
    # variance of [1,2,3] = 1 (sample variance)
    assert round(variance([1, 2, 3]), 2) == 1.00

def test_standard_deviation():
    # stdev of [1,2,3] = sqrt(1) = 1
    assert round(standard_deviation([1, 2, 3]), 2) == 1.00
