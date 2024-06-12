import math
import pytest

# テスト対象の関数
def classify(a: float) -> str:
    if a < 0.15:
        return "LOW"
    if a <= 0.85:
        return "MIDDLE"
    else:
        return "HIGH"


# テストのパラメータ化
@pytest.mark.parametrize("test_param, expected", [
    (math.nextafter(0.15, 0.0), "LOW"),
    (0.15, "MIDDLE"),
    (0.85, "MIDDLE"),
    (math.nextafter(0.85, 1.0), "HIGH"),
])
def test_add(test_param: float, expected: str):
    assert classify(test_param) == expected
