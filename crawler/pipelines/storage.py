import os
from datetime import datetime

class DataStorage:
    """数据存储管道"""
    
    def __init__(self):
        self.output_dir = 'data'
        os.makedirs(self.output_dir, exist_ok=True)

    def save_to_csv(self, data):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        path = os.path.join(self.output_dir, f'{timestamp}_output.csv')
        with open(path, 'w', newline='') as f:
            f.write('URL,Content\n')
            for item in data: f.write(f'{item["url"]},{item["content"]}\n')
        return path
