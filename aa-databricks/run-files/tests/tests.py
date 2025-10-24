from src.run_files import get_all_file_paths


def test_get_all_files_one_level():
    files = get_all_file_paths(
        "",
        lambda _: ["filea", "fileb", "filec"],
        lambda item, _path: item,
        lambda _: False,
        lambda _: True,
    )
    assert files == ["filea", "fileb", "filec"]


def test_get_all_files_recursive():
    files = get_all_file_paths(
        "",
        lambda path: {
            "": ["filea", "dir1"],
            "dir1": ["fileb", "dir2"],
            "dir1/dir2": ["filec"],
        }[path],
        lambda item, path: f"{path}/{item}".strip("/"),
        lambda item: "dir" in item,
        lambda item: "file" in item,
        ["", "dir1/fileb"],
    )
    assert files == ["filea", "dir1/dir2/filec"]
