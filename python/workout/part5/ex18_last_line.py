from pathlib import Path


def get_final_line(file_name):


def test_final_line_mine():
    file_name = Path(__file__).parent / "ex18.txt"
    result = get_final_line(file_name)
    
    assert result == "line 4"
