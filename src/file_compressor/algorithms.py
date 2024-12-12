import gzip
import lzma
import bz2
import shutil
from .interface import CompressionAlgorithm

class GzipCompress(CompressionAlgorithm):
    def compress(self, inputfilepath: str, outputfilepath: str):
        with (open(inputfilepath, 'rb') as f_in,
              gzip.open(outputfilepath, 'wb') as f_out):
            shutil.copyfileobj(f_in, f_out)

    def decompress(self, inputfilepath: str, outputfilepath: str):
        with (gzip.open(inputfilepath, 'rb') as f_in,
              open(outputfilepath, 'wb') as f_out):
            shutil.copyfileobj(f_in, f_out)

class Bz2Compress(CompressionAlgorithm):
    def compress(self, inputfilepath: str, outputfilepath: str):
        with (open(inputfilepath, 'rb') as f_in,
              bz2.open(outputfilepath, 'wb') as f_out):
            shutil.copyfileobj(f_in, f_out)

    def decompress(self, inputfilepath: str, outputfilepath: str):
        with (bz2.open(inputfilepath, 'rb') as f_in,
              open(outputfilepath, 'wb') as f_out):
            shutil.copyfileobj(f_in, f_out)

class LzmaCompress(CompressionAlgorithm):
    def compress(self, inputfilepath: str, outputfilepath: str):
        with (open(inputfilepath, 'rb') as f_in,
              lzma.open(outputfilepath, 'wb') as f_out):
            shutil.copyfileobj(f_in, f_out)

    def decompress(self, inputfilepath: str, outputfilepath: str):
        with (lzma.open(inputfilepath, 'rb') as f_in,
              open(outputfilepath, 'wb') as f_out):
            shutil.copyfileobj(f_in, f_out)