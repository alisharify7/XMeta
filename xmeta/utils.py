"""
* X Meta
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/XMeta
"""

import os
import mimetypes

try:
    import magic  # python-magic, optional for better MIME detection
except ImportError:
    magic = None


def detect_type(file_path: str) -> str:
    """
    Detects the general media type of a file based on MIME type or extension.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: One of "image", "video", "audio", "document", or "unknown".
    """
    if magic:
        try:
            mime_type = magic.from_file(file_path, mime=True)
        except Exception:
            mime_type = None
    else:
        mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type is None:
        ext = os.path.splitext(file_path)[1].lower()
        # Basic fallback by extension
        if ext in {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}:
            return "image"
        elif ext in {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"}:
            return "video"
        elif ext in {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"}:
            return "audio"
        elif ext in {".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"}:
            return "document"
        else:
            return "unknown"

    # MIME type mapping
    if mime_type.startswith("image/"):
        return "image"
    elif mime_type.startswith("video/"):
        return "video"
    elif mime_type.startswith("audio/"):
        return "audio"
    elif mime_type in {
        "application/pdf",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-powerpoint",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    }:
        return "document"
    else:
        return "unknown"
