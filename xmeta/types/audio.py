"""
* X Meta
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/XMeta
"""

import mutagen
from xmeta.base import BaseMetadataHandler


class AudioMetadataHandler(BaseMetadataHandler):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.audio = mutagen.File(filepath, easy=True)
        if self.audio is None:
            raise ValueError("Unsupported or corrupted audio file.")

    def read(self) -> dict:
        return dict(self.audio)

    def update(self, updates: dict) -> None:
        for key, value in updates.items():
            self.audio[key] = value

    def delete(self, keys: list) -> None:
        for key in keys:
            if key in self.audio:
                del self.audio[key]

    def save(self, output_path: str = None) -> None:
        self.audio.save(output_path or self.filepath)
