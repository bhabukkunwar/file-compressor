import pytest
from unittest.mock import MagicMock
from src.file_compressor import FileCompress, CompressFactory


# Mock the compression classes
@pytest.fixture
def mock_compression_classes():
    # Create mock objects for the algorithms
    mock_gzip = MagicMock()
    mock_bz2 = MagicMock()
    mock_lzma = MagicMock()

    # Mock CompressFactory to return mocked classes
    CompressFactory.get_compression_algo = MagicMock(side_effect=lambda algorithm: {
        'gzip': mock_gzip,
        'bz2': mock_bz2,
        'lzma': mock_lzma
    }.get(algorithm, ValueError("Unsupported algorithm")))

    return mock_gzip, mock_bz2, mock_lzma


# Test correct algorithm selection and compression
def test_compress(mock_compression_classes):
    mock_gzip, mock_bz2, mock_lzma = mock_compression_classes

    # Test with gzip
    file_compress_gzip = FileCompress("gzip")
    file_compress_gzip.compress("input.txt", "output.gz")
    mock_gzip.compress.assert_called_once_with("input.txt", "output.gz")

    # Test with bz2
    file_compress_bz2 = FileCompress("bz2")
    file_compress_bz2.compress("input.txt", "output.bz2")
    mock_bz2.compress.assert_called_once_with("input.txt", "output.bz2")

    # Test with lzma
    file_compress_lzma = FileCompress("lzma")
    file_compress_lzma.compress("input.txt", "output.lzma")
    mock_lzma.compress.assert_called_once_with("input.txt", "output.lzma")


# Test decompression
def test_decompress(mock_compression_classes):
    mock_gzip, mock_bz2, mock_lzma = mock_compression_classes

    # Test with gzip
    file_compress_gzip = FileCompress("gzip")
    file_compress_gzip.decompress("input.gz", "output.txt")
    mock_gzip.decompress.assert_called_once_with("input.gz", "output.txt")

    # Test with bz2
    file_compress_bz2 = FileCompress("bz2")
    file_compress_bz2.decompress("input.bz2", "output.txt")
    mock_bz2.decompress.assert_called_once_with("input.bz2", "output.txt")

    # Test with lzma
    file_compress_lzma = FileCompress("lzma")
    file_compress_lzma.decompress("input.lzma", "output.txt")
    mock_lzma.decompress.assert_called_once_with("input.lzma", "output.txt")


# Test invalid algorithm handling
def test_invalid_algorithm():
    file_compress = FileCompress("unsupported_algo")

    # Mocking the method to check if error is handled correctly
    with pytest.raises(ValueError, match="Unsupported compression algorithm: unsupported_algo"):
        file_compress.compress("input.txt", "output.txt")

    with pytest.raises(ValueError, match="Unsupported compression algorithm: unsupported_algo"):
        file_compress.decompress("input.txt", "output.txt")