"""
* X Meta
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/XMeta
"""

import os
import typing
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
from xmeta.base import BaseMetadataHandler


class ImageMetadataHandler(BaseMetadataHandler):
    def __init__(self, file_path: str | os.PathLike | Path):
        if isinstance(file_path, str): 
            file_path = Path(file_path)
        
        self.file_path = file_path
        self.file_name = file_path.name 
        self.file_extension = file_path.suffix
        self.file_content = Image.open(file_path)


    def _extract_metadata(self) -> dict:
        readable = {}
        if self.exif_dict:
            for tag_id, value in self.exif_dict.items():
                tag = TAGS.get(tag_id, tag_id)
                print(f"{tag}: {value}")

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


    def info(self):
        image_metadata_support = {
            "jpg": {
                "metadata_types": ["EXIF", "IPTC", "XMP"],
                "notes": "Most common photo format; widely used for digital photos; supports rich metadata."
            },
            "jpeg": {
                "metadata_types": ["EXIF", "IPTC", "XMP"],
                "notes": "Most common photo format; widely used for digital photos; supports rich metadata."
            },
            "tif": {
                "metadata_types": ["EXIF", "IPTC", "XMP"],
                "notes": "Professional imaging format; supports multiple metadata standards; large files."
            },
            "tiff": {
                "metadata_types": ["EXIF", "IPTC", "XMP"],
                "notes": "Professional imaging format; supports multiple metadata standards; large files."
            },
            "png": {
                "metadata_types": ["tEXt", "iTXt", "zTXt chunks", "XMP"],
                "notes": "Lossless compression; no EXIF support; text chunks for textual metadata; supports XMP."
            },
            "gif": {
                "metadata_types": ["Comment"],
                "notes": "Limited metadata support; mainly comment strings; no EXIF or IPTC."
            },
            "bmp": {
                "metadata_types": [],
                "notes": "Simple format; almost no metadata support."
            },
            "webp": {
                "metadata_types": ["XMP (experimental)"],
                "notes": "Modern format by Google; metadata support is evolving; limited EXIF support."
            },
            "heif": {
                "metadata_types": ["EXIF", "XMP"],
                "notes": "Newer format for photos on mobile devices; supports rich metadata similar to JPEG."
            },
            "heic": {
                "metadata_types": ["EXIF", "XMP"],
                "notes": "Newer format for photos on mobile devices; supports rich metadata similar to JPEG."
            },
            "raw": {
                "metadata_types": ["EXIF", "IPTC", "XMP"],
                "notes": "Manufacturer-specific; professional use; contains detailed camera metadata."
            },
            "psd": {
                "metadata_types": ["XMP"],
                "notes": "Adobe Photoshop native format; supports rich metadata in XMP format."
            },
            "pdf": {
                "metadata_types": ["XMP", "Custom metadata"],
                "notes": "Not strictly image format; can embed images with metadata inside documents."
            }
        }
        if self.file_extension.lower() in image_metadata_support:
            print(image_metadata_support[self.file_extension.lower()])

        #TODO: add size, file name, type, etc
        


# | Image Format            | Supported Metadata Types     | Notes                                                                                  |
# | ----------------------- | ---------------------------- | -------------------------------------------------------------------------------------- |
# | **JPEG / JPG**          | EXIF, IPTC, XMP              | Most common photo format; widely used for digital photos; supports rich metadata.      |
# | **TIFF / TIF**          | EXIF, IPTC, XMP              | Professional imaging format; supports multiple metadata standards; large files.        |
# | **PNG**                 | tEXt, iTXt, zTXt chunks, XMP | Lossless compression; no EXIF support; text chunks for textual metadata; supports XMP. |
# | **GIF**                 | Comment                      | Limited metadata support; mainly comment strings; no EXIF or IPTC.                     |
# | **BMP**                 | None (very limited)          | Simple format; almost no metadata support.                                             |
# | **WEBP**                | XMP (experimental)           | Modern format by Google; metadata support is evolving; limited EXIF support.           |
# | **HEIF / HEIC**         | EXIF, XMP                    | Newer format for photos on mobile devices; supports rich metadata similar to JPEG.     |
# | **RAW formats**         | EXIF, IPTC, XMP              | Manufacturer-specific; professional use; contains detailed camera metadata.            |
# | **PSD**                 | XMP                          | Adobe Photoshop native format; supports rich metadata in XMP format.                   |
# | **PDF (images inside)** | XMP, Custom metadata         | Not strictly image format; can embed images with metadata inside documents.            |
