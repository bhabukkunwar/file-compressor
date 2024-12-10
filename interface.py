from abc import ABC, abstractstaticmethod, abstractmethod

class CompressionAlgorithm(ABC):
    @abstractmethod
    def compress(self, inputfilepath: str, outputfilepath: str):
        """Compress the input file"""
        pass
    @abstractmethod
    def decompress(self, inputfilepath: str, outputfilepath: str):
        """Decompress the input file"""
        pass