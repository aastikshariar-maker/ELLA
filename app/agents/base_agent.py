"""Base Agent Abstract Class"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """Abstract base class for all agents"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.memory: Dict[str, Any] = {}
    
    @abstractmethod
    async def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze data and provide insights"""
        pass
    
    @abstractmethod
    async def recommend(self, context: Dict[str, Any]) -> List[str]:
        """Generate recommendations based on context"""
        pass
    
    def store_memory(self, key: str, value: Any):
        """Store information in agent memory"""
        self.memory[key] = value
        logger.debug(f"{self.name} stored: {key}")
    
    def retrieve_memory(self, key: str) -> Any:
        """Retrieve stored information"""
        return self.memory.get(key)
    
    async def __call__(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make agent callable"""
        return await self.analyze(data)
