from dataclasses import dataclass

from src.datalayers.base import RepositoryInterface

@dataclass
class ServiceBase:
    repository: RepositoryInterface