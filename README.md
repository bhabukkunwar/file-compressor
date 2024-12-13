# File Compressor

File Compressor is a flexible Python library that provides a simple interface for compressing and decompressing files using multiple compression algorithms, including gzip, bz2, lzma.

## Features
- Support for multiple compression algorithms:
    - gzip
    - bz2
    - lzma
- Factory pattern for algorithm selection
- Easy-to-use compression and decompression methods

## Installation
### Prerequisites
- Python 3.10+

### From GitHub Releases (Recommended)
1. Go to the Releases page
2. Download the latest .whl file
3. Install using pip:
    ```bash
    pip install file_compressor-*.whl
    ```

### From Source
```bash
git clone https://github.com/bhabukkunwar/file-compressor.git
cd file-compressor
pip install 
```

## Usage
### Compression Example
```python
from file_compressor import FileCompress
# Compress using Gzip
compressor = FileCompress(algorithm="gzip")
compressor.compress("<input-file-to-compress-path>", "<outputfilepath>")
```

### Decompression Example
```python
# Decompress Gzip file
compressor.decompress("<input-file-to-decompress-path>", "<outputfilepath>")
```

## Supported Algorithms
| Algorithm         | Description                     |
|-------------------|---------------------------------|
| gzip             | Standard compression algorithm  |
| bz2              | Bzip2 compression algorithm     |
| lzma             | LZMA compression algorithm      |






