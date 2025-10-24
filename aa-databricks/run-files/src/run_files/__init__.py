import hashlib
import logging
from typing import Callable

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_all_file_paths(
    path: str,
    get_items: Callable[[str], list[object]],
    get_item_path: Callable[[object, str], str],
    is_dir: Callable[[object], bool],
    is_file: Callable[[object], bool],
    excluded_files: list[str] = [],
) -> list[str]:
    files: list[str] = []

    items = get_items(path)
    for item in items:
        if is_dir(item):
            files.extend(
                get_all_file_paths(
                    get_item_path(item, path),
                    get_items,
                    get_item_path,
                    is_dir,
                    is_file,
                )
            )
        elif is_file(item):
            files.append(get_item_path(item, path))

    for excluded_file in excluded_files:
        if excluded_file in files:
            files.remove(excluded_file)
        else:
            logging.warning(f"Excluded file '{excluded_file}' not in existing files")

    return files


def calculate_file_hash(file_contents) -> bytearray:
    return bytearray(hashlib.sha256(file_contents).digest())


def run_files(
    file_paths: list[str],
    has_ran: Callable[[str], bool],
    has_changed: Callable[[str], bool],
    run_file: Callable[[str], None],
    file_ran: Callable[[str], None],
):
    total_files = len(file_paths)
    failed_files: list[str] = []
    skipped_files: list[str] = []

    for file_path in file_paths:
        if has_ran(file_path) and not has_changed(file_path):
            skipped_files.append(file_path)
            logging.info(f"Skipped file (already ran and not changed): {file_path}")
            continue

        try:
            logging.info(
                f"Running file ({'has not ran/failed to run' if not has_ran(file_path) else 'has changed'}): {file_path}"
            )
            run_file(file_path)
            file_ran(file_path)
        except Exception as e:
            logging.warning(f"Failed to run file {file_path}, got error: {e}")

    if len(skipped_files) == total_files:
        logging.warning("All notebooks were skipped")
    elif len(skipped_files) > 0:
        logging.info(
            f"Skipped notebooks (already ran and not changed): {skipped_files} ({len(skipped_files)} of {total_files})"
        )
        if len(failed_files) > 0:
            text = f"Failed to run files: {failed_files} ({len(failed_files)} of {total_files})"
            logging.warning(text)
            raise Exception(text)
