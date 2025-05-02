import os
from typing import Dict
import yaml

class ConfigManager:
    """配置管理器"""
    
    def __init__(self, config_file='config.yaml'):
        self.config_file = config_file
        self.config = self._load_default_config()
        
    def _load_default_config(self) -> Dict:
        """加载默认配置"""
        return {
            'request': {
                'headers': {
                    'User-Agent': 'CrawlerLibrary/2.0',
                    'Accept-Language': 'en-US,en;q=0.9'
                },
                'timeout': 10.0,
                'verify_ssl': True,
                'concurrency': 5
            },
            'logging': {
                'level': 'INFO',
                'file': 'crawler.log'
            }
        }
        
    def get_config(self) -> Dict:
        """获取当前配置"""
        return self.config
        
    def update_config(self, new_config: Dict):
        """更新配置"""
        self.config.update(new_config)
        