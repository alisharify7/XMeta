"""
* X Meta
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/XMeta
"""

import subprocess
import json
from typing import Optional
from xmeta.base import BaseMetadataHandler


class VideoMetadataHandler(BaseMetadataHandler):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.metadata = self._get_metadata()

    def _get_metadata(self) -> dict:
        result = subprocess.run(
            [
                "ffprobe",
                "-v",
                "quiet",
                "-print_format",
                "json",
                "-show_format",
                self.filepath,
            ],
            capture_output=True,
            text=True,
        )
        return json.loads(result.stdout).get("format", {}).get("tags", {})

    def read(self) -> dict:
        return self.metadata

    def update(self, updates: dict) -> None:
        raise NotImplementedError("Updating video metadata is not yet supported.")

    def delete(self, keys: list) -> None:
        raise NotImplementedError("Deleting video metadata is not yet supported.")

    def save(self, output_path: Optional[str] = None) -> None:
        raise NotImplementedError("Saving video metadata is not yet supported.")
