from algorithms import GzipCompress, Bz2Compress, LzmaCompress

class CompressFactory:
    @staticmethod
    def get_compression_algo(algorithm: str):
        if algorithm == "gzip":
            return GzipCompress()
        if algorithm == "bz2":
            return  Bz2Compress()
        if algorithm == "lzma":
            return  LzmaCompress()
        raise ValueError(f"Unsupported compression algorithm: {algorithm}")

class FileCompress:
    def __init__(self, algorithm: str):
        self.algorithm = algorithm
        self.factory = CompressFactory()

    def compress(self, inputfilepath: str, outputfilepath: str):
        try:
            algorithm = self.factory.get_compression_algo(self.algorithm)
            algorithm.compress(inputfilepath,outputfilepath)
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error during compression: {e}")

    def decompress(self, inputfilepath: str, outputfilepath: str):
        try:
            algorithm = self.factory.get_compression_algo(self.algorithm)
            algorithm.decompress(inputfilepath, outputfilepath)
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error during compression: {e}")
