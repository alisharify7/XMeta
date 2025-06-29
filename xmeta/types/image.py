"""
* X Meta
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/XMeta
"""

from PIL import Image
import piexif
from xmeta.base import BaseMetadataHandler


class ImageMetadataHandler(BaseMetadataHandler):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.image = Image.open(file_path)
        # Load EXIF dict, if no exif info, initialize empty structure
        exif_bytes = self.image.info.get("exif", b"")
        if exif_bytes:
            self.exif_dict = piexif.load(exif_bytes)
        else:
            self.exif_dict = {
                "0th": {},
                "Exif": {},
                "GPS": {},
                "Interop": {},
                "1st": {},
                "thumbnail": None,
            }
        self.metadata = self._extract_metadata()

    def _extract_metadata(self) -> dict:
        readable = {}
        for ifd_name in self.exif_dict:
            if self.exif_dict[ifd_name] is None:
                continue
            for tag, value in self.exif_dict[ifd_name].items():
                tag_name = piexif.TAGS[ifd_name][tag]["name"]
                # Decode bytes if possible for strings
                if isinstance(value, bytes):
                    try:
                        value = value.decode("utf-8")
                    except UnicodeDecodeError:
                        pass
                readable[tag_name] = value
        return readable

    def read(self) -> dict:
        return self.metadata

    def update(self, new_metadata: dict):
        """
        Updates metadata in-memory. Call save() to persist changes.
        Encodes string values properly for EXIF.
        """
        for ifd_name in self.exif_dict:
            if ifd_name not in piexif.TAGS:
                continue
            for tag, tag_info in piexif.TAGS[ifd_name].items():
                tag_name = tag_info["name"]
                if tag_name in new_metadata:
                    val = new_metadata[tag_name]
                    if isinstance(val, str):
                        val = val.encode("utf-8")
                    self.exif_dict[ifd_name][tag] = val
        self.metadata = self._extract_metadata()

    def delete(self, keys: list[str]):
        for key in keys:
            for ifd_name in self.exif_dict:
                if self.exif_dict[ifd_name] is None:
                    continue
                tags_to_delete = []
                for tag, value in self.exif_dict[ifd_name].items():
                    tag_name = piexif.TAGS[ifd_name][tag]["name"]
                    if tag_name == key:
                        tags_to_delete.append(tag)
                for tag in tags_to_delete:
                    del self.exif_dict[ifd_name][tag]
        self.metadata = self._extract_metadata()

    def save(self, output_path: str = None):
        """
        Saves image with updated EXIF metadata.
        Converts image mode to RGB if needed for JPEG saving.
        """
        if self.image.mode in ("RGBA", "P"):
            self.image = self.image.convert("RGB")
        exif_bytes = piexif.dump(self.exif_dict)
        target_path = output_path or self.file_path
        self.image.save(target_path, exif=exif_bytes)
