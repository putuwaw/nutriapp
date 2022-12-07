from modules import branch_and_bound as bnb

def test_bnb():
    result = bnb.solve(10, "A, 3, 12\r\nB, 7, 42\r\nC, 5, 25\r\nD, 4, 40")
    assert result[0] == 65.0
    assert result[1] == ["D", "C"]

    result = bnb.solve(10, "A, 2, 40\r\nB, 3.14, 50\r\nC, 1.98, 100\r\nD, 5, 95\r\nE, 3, 30")
    assert result[0] == 235.0
    assert result[1] == ["C", "A", "D"]

    result = bnb.solve(40, "A, 30, 10\r\nB, 10, 20\r\nC, 40, 30\r\nD, 20, 40")
    assert result[0] == 60.0
    assert result[1] == ["B", "D"]

    result = bnb.solve(8, "A, 3, 2\r\nB, 4, 3\r\nC, 6, 1\r\nD, 5, 4")
    assert result[0] == 6.0
    assert result[1] == ["D", "A"]