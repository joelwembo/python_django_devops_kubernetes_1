class InfiniteCounter:
    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        self.count += 1
        return self.count

for num in InfiniteCounter():
    if num > 5:
        break
    print(num)  # This will print 1 to 5
    
class FileSimulator:
    def __enter__(self):
        print("Opening file...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")

with FileSimulator():
    print("Inside the context")