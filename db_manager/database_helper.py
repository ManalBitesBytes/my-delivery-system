from abc import ABC, abstractmethod

class DatabaseHelper(ABC):
    @abstractmethod
    def get(self, query, params=None):
        pass

    @abstractmethod
    def set(self, query, params=None):
        pass

    @abstractmethod
    def close(self):
        pass
