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

class FileCompress:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.factory = CompressFactory()

    def compress(self, inputfilepath: str, outputfilepath: str):
        algorithm = self.factory.get_compression_algo(self.algorithm)
        algorithm.compress(inputfilepath,outputfilepath)

    def decompress(self, inputfilepath: str, outputfilepath: str):
        algorithm = self.factory.get_compression_algo(self.algorithm)
        algorithm.decompress(inputfilepath, outputfilepath)