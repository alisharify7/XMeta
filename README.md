# 💫 XMeta

<img src="./docs/xmeta2.png" width="400" alt="XMeta Logo">

**XMeta** is a powerful and extensible Python package for performing CRUD operations on media metadata.  
It supports a wide range of file types including images, videos, audio files, and documents.

---

## ✨ Features

- ✅ Unified interface to **read**, **update**, and **delete** metadata
- 🖼️ Supports **images** (`.jpeg`, `.png`, etc.)
- 🎞️ Supports **videos** (`.mp4`, `.mkv`, etc.)
- 🎧 Supports **audio files** (`.mp3`, `.flac`, etc.)
- 📄 Supports **documents** (`.pdf`, `.docx`, etc.)
- 🧠 Automatic file type detection via MIME type and file extension
- 🔌 Easily extensible with **custom handlers**

---

## 📦 Installation

> XMeta is not yet published on PyPI. You can install it locally for development:

```bash
pip install xmeta  # Coming soon to PyPI
```

---

## 🛠️ Usage Guide

XMeta offers a simple and consistent interface to interact with media metadata.

---

### ✅ 1. Initialize the Metadata Manager

Create an instance of `XmetaMetadataManager` by passing the file path:

```python
from xmeta import XmetaMetadataManager

file_meta = XmetaMetadataManager("path/to/your/file")
```

---

### ✅ 2. Read Metadata

Retrieve and inspect the metadata of the file:

```python
metadata = file_meta.read()
print(metadata)
```

> ℹ️ Returns a dictionary of key-value pairs representing the file's metadata.

---

### ✅ 3. Update Metadata

Modify or add metadata by passing a new dictionary:

```python
file_meta.update(new_metadata={
    "Author": "Ali Sharify",
    "Description": "Sample image"
})
```

> ⚠️ This replaces the existing metadata fields with the new values provided.

---

### ✅ 4. Save the Changes

Write the updated metadata back to a file. You can either overwrite the original or write to a new file:

```python
file_meta.save(output_path="updated_file.jpg")  # Saves to a new file
```

If `output_path` is **not** provided, the original file will be **overwritten**.

---

## 🧪 Example

A complete usage example:

```python
from xmeta import XmetaMetadataManager

meta = XmetaMetadataManager("sample.jpg")

# Read existing metadata
print(meta.read())

# Update selected fields
meta.update({
    "Title": "Sunset Photo",
    "Location": "Caspian Sea"
})

# Save changes to a new file
meta.save("sunset_updated.jpg")
```

---

## 📚 Coming Soon

- 🧰 **Command-line interface** (CLI) for quick metadata editing  
- 🔌 **Plugin system** for extending media type support  
- 🖥️ **Web dashboard** for managing metadata visually

---

## 👨‍💻 Author

Developed with ❤️ by [Ali Sharify](https://github.com/alisharify7)  
Proudly maintained by the [Free Developers](https://github.com/free-programmers) organization.

---

## 📄 License

This project is licensed under the GNU License.
