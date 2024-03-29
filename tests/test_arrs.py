from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1,2,3], -3, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0, 5) == []
    assert arrs.my_slice ([1, 2, 3, 4], 1, 6) == [2, 3, 4]
    assert arrs.my_slice ([1, 2, 3, 4], 1, -10) == []
    assert arrs.my_slice ([1, 2, 3, 4], 3, 1) == []
    assert arrs.my_slice ([1, 2, 3, 4], -3, 1) == [2,3,4]
    assert arrs.my_slice ([1, 2, 3, 4], -5, 1) == [1,2,3,4]
    assert arrs.my_slice ([1, 2, 3, 4], 0, -2) == []
    assert arrs.my_slice ([1, 2, 3, 4], -1) == "Ошибка, необходимо задать числовое значение для end"
    assert arrs.my_slice ([1, 2, 3, 4], -2, -3) == []
    assert arrs.my_slice ([1, 2, 3, 4], -2, -2) == []
    assert arrs.my_slice ([1, 2, 3, 4], 1, -2) == []
    assert arrs.my_slice ([], 0) == []

