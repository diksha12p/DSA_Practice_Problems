class ArrayLists:
    def __init__(self, value = 10):
        self.max_size = value
        self.curr_size = 0
        self.list = [None] * self.max_size

    # Adding a value at the end of the array
    def add(self, value):
        if self.curr_size >= self.max_size:
            self._increase_size()
        self.list[self.curr_size] = value
        self.curr_size += 1

    def _increase_size(self):
        new_list_size = self.max_size * 2
        new_list = [None] * new_list_size
        for i in range(0,self.max_size):
            new_list[i] = self.list[i]
        self.max_size = new_list_size
        self.list = new_list

    def delete(self, index):
        if index >= self.curr_size or index < 0:
            raise Exception("Index out of bounds!")
        else:
            self.list[index] = self.list[index+1]
            self.curr_size -= 1

    def get(self, index):
        if index >= self.curr_size or index < 0:
            raise Exception("Index out of bounds!")
        else:
            return self.list[index]


nums = ArrayLists(value=1)

nums.add(1)
nums.add(2)
# print(nums.curr_size, nums.max_size)
nums.add(3)
# print(nums.curr_size, nums.max_size)
