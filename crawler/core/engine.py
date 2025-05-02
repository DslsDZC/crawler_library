import queue
import threading

class RequestEngine:
    """请求调度引擎"""
    
    def __init__(self, max_workers=5):
        self.queue = queue.Queue()
        self.workers = []
        self.max_workers = max_workers
        
    def add_task(self, task):
        """添加任务到队列"""
        self.queue.put(task)
        
    def start(self):
        """启动工作线程"""
        for _ in range(self.max_workers):
            worker = threading.Thread(target=self._worker_loop)
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
            
    def _worker_loop(self):
        """工作线程主循环"""
        while True:
            task = self.queue.get()
            if task is None: break
            try:
                task.execute()
            except Exception as e:
                print(f"任务执行失败: {str(e)}")
            finally:
                self.queue.task_done()
                
    def shutdown(self):
        """关闭引擎"""
        for _ in range(self.max_workers):
            self.queue.put(None)
        for worker in self.workers:
            worker.join()
