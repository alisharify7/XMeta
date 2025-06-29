"""
* X Meta
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/XMeta
"""

import fitz  # PyMuPDF
from xmeta.base import BaseMetadataHandler


class DocumentMetadataHandler(BaseMetadataHandler):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.doc = fitz.open(filepath)

    def read(self) -> dict:
        return dict(self.doc.metadata)

    def update(self, updates: dict) -> None:
        self.doc.set_metadata({**self.doc.metadata, **updates})

    def delete(self, keys: list) -> None:
        current = dict(self.doc.metadata)
        for key in keys:
            current.pop(key, None)
        self.doc.set_metadata(current)

    def save(self, output_path: str = None) -> None:
        self.doc.save(output_path or self.filepath)
        self.doc.close()
