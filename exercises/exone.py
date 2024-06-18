class Solutions:

    def __init__(self, nums_list, target_number):
        self.nums_list = nums_list
        self.target_number = target_number
        self.index_counter = 0
        self.evaluation_number = 0
        self.target_comparator = 0

    def for_sol(self):
        for i in self.nums_list:
            # self.evaluation_number = self.nums_list[self.index_counter]
            for a in self.nums_list:
                self.target_comparator = i + a
                if self.target_comparator == self.target_number:
                    print(f'[{self.index_counter}, {self.nums_list.index(a)}]')

            self.index_counter += 1

    def sol_two(self):
        for i in self.nums_list:
            print('call')


my_nums = [2, 4, 3, 7, 10, 11]
test_one = Solutions(my_nums, 9)
test_one.for_sol()
