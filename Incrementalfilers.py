class CumulativeSumFilter:
    def __init__(self):
        self.cumulative_sum = 0

    def update(self, new_data):
        self.cumulative_sum += new_data
        return self.cumulative_sum

# Example usage
filter = CumulativeSumFilter()
data = [1, 2, 3, 4, 5]

for num in data:
    result = filter.update(num)
    print(f"Cumulative Sum: {result}")
