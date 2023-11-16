#!/usr/bin/env python3

import os


def create_output_dirs_from_file_path(output_file: str) -> None:
    dir = os.path.dirname(output_file)
    if os.path.exists(dir):
        return

    os.makedirs(dir)

