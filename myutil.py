class MyUtil:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def print_array(array):

        row_length = len(array)
        col_length = len(array[0])

        for i in range(row_length):
            for j in range(col_length):
                if array[i][j] == 1:
                    print(MyUtil.FAIL, array[i][j], MyUtil.ENDC, end=" ")
                else:
                    print(MyUtil.BOLD, array[i][j], MyUtil.ENDC, end=" ")
            print()
