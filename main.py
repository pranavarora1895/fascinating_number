class Fascinating:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def mul_concat(self):
        a = self * 1
        b = self * 2
        c = self * 3
        return str(a) + str(b) + str(c)

    def calc_fascinating(self):
        res_num = Fascinating.mul_concat(self)
        # print((res_num))
        ref_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        check_array = []
        num_check_array = []
        for character in res_num:
            if int(character) in ref_array:
                if character in check_array:
                    continue
                check_array.append(character)
        [num_check_array.append(int(i)) for i in check_array]
        num_check_array.sort()
        if ref_array == num_check_array:
            return self

    def get_range(self):
        count = 0
        for i in range(self.start, self.end):
            fascinating_number = Fascinating.calc_fascinating(i)
            if fascinating_number:
                count += 1
                print(fascinating_number)
        print("Frequency: ", count)


if __name__ == '__main__':
    start_range = int(input("Enter the start range: "))
    end_range = int(input("Enter the end range: "))

    fascinating_num = Fascinating(start_range, end_range)
    fascinating_num.get_range()
