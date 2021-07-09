class Timer:
    import time

    def __enter__(self):
        self.start_time=self.time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.time.time()-self.start_time)

with Timer() as t:
    for i in range(10000000):
        pass
