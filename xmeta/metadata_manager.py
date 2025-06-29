"""
* X Meta
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/XMeta
"""

from xmeta.types import image, video, audio, document
from xmeta.utils import detect_type


class XmetaMetadataManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.handler = self._get_handler()

    def _get_handler(self):
        file_type = detect_type(self.file_path)
        match file_type:
            case "image":
                return image.ImageMetadataHandler(self.file_path)
            case "video":
                return video.VideoMetadataHandler(self.file_path)
            case "audio":
                return audio.AudioMetadataHandler(self.file_path)
            case "document":
                return document.DocumentMetadataHandler(self.file_path)
            case _:
                raise ValueError(f"Unsupported file type: {file_type}")

    def read(self):
        return self.handler.read()

    def update(self, new_metadata: dict):
        return self.handler.update(new_metadata)

    def delete(self, keys: list[str]):
        return self.handler.delete(keys)

    def save(self, output_path: str = None):
        return self.handler.save(output_path or self.file_path)
