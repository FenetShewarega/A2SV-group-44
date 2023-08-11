
class MedianFinder:
    
    def __init__(self):
        self.data = list()

    def addNum(self, num: int) -> None:
        self.data.append(num)
        return

    def findMedian(self) -> float:
        half = len(self.data) // 2
        self.data.sort()
        if not len(self.data) % 2:
            return (self.data[half - 1] + self.data[half]) / 2.0
        return float(self.data[half])