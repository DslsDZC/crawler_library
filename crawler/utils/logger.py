import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file='crawler.log', level=logging.INFO):
    """配置日志记录器"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # 文件处理器（支持日志轮转）
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger
