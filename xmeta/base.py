"""
* X Meta
* author: github.com/alisharify7
* email: alisharifyofficial@gmail.com
* license: see LICENSE for more details.
* Copyright (c) 2025 - ali sharifi
* https://github.com/alisharify7/XMeta
"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseMetadataHandler(ABC):
    """
    Abstract base class for all metadata handlers in Xmeta.

    Defines a unified interface for reading, updating, deleting,
    and saving metadata for different media types.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    @abstractmethod
    def read(self) -> dict:
        """
        Read metadata from the file.

        Returns:
            dict: Extracted metadata.
        """
        pass

    @abstractmethod
    def update(self, updates: dict) -> None:
        """
        Update metadata with given key-value pairs.

        Args:
            updates (dict): Metadata keys and values to update.
        """
        pass

    @abstractmethod
    def delete(self, keys: list) -> None:
        """
        Delete specified metadata fields.

        Args:
            keys (list): List of metadata keys to remove.
        """
        pass

    @abstractmethod
    def save(self, output_path: Optional[str] = None) -> None:
        """
        Save changes to the file or optionally to a new file.

        Args:
            output_path (Optional[str]): Destination file path.
        """
        pass
