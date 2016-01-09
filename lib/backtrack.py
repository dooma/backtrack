__author__ = 'Călin Sălăgean'


class Backtrack():
    '''
    Class provides permutations of any list with a specified rule. Every rule should be implemented
    Candidate list is a list with unique elements
    '''

    def __init__(self, array):
        '''
        Class constructor
        :param array: The list that should be reordered
        :return:
        '''
        self.validate(array)
        self.__array = array
        self.__result = []
        self.__permutation = []

    @staticmethod
    def validate(array):
        '''
        Validation method
        :param array:
        :return:
        :raise AttributeError: If array is not a list
        :raise ValueError: If elements from array are not integers or floats
        '''
        if type(array) is not list or not len(array):
            raise AttributeError("'input' attribute should be a list")

        for elem in array:
            try:
                int(elem)
                float(elem)
            except ValueError:
                error_message = "The element on position {} should be integer or float number".format(array.index(elem))
                raise ValueError(error_message)

    @property
    def array(self):
        '''
        :return: List provided at constructor
        '''
        return self.__array

    @property
    def result(self):
        '''
        :return: List with results
        '''
        return self.__result

    def reset_result(self):
        '''
        Initialize result with empty list. Needed if don't want to append to already generated solutions
        :return: None
        '''
        self.__result = []

    @property
    def minimum_value(self):
        '''
        :return: Minimum value from array
        '''
        return min(self.__array)

    def determine(self, index = 0, method = 'valley'):
        '''
        Generates all solutions for given method.
        Implements backtracking algorithm using recursive call.
        :param index: Position in array
        :param method: Given algorithm that a candidate list should match to be a solution
        :return: None
        '''
        if index == len(self.array):
            if getattr(self, method)():
                self.__result.append(self.construct_permutation())
        else:
            for elem in range(len(self.array)):
                if not elem in self.__permutation:
                    self.__permutation.append(elem)
                    self.determine(index + 1)
                    self.__permutation.pop()

    def determine_inline(self, method = 'valley'):
        '''
        Generates all solutions for given method.
        Implements backtracking algorithm using recursive call.
        :param method: Given algorithm that a candidate list should match to be a solution
        :return: None
        '''
        self.__permutation = [-1]

        while len(self.__permutation):
            choosed = False
            elem = self.__permutation[-1]

            while not choosed and elem < len(self.__array) - 1:
                elem += 1
                choosed = elem not in self.__permutation

            if choosed:
                self.__permutation.pop()
                self.__permutation.append(elem)
                if len(self.__permutation) == len(self.__array) and getattr(self, method)():
                    self.__result.append(self.construct_permutation())
                self.__permutation.append(-1)
            else:
                self.__permutation.pop()

    def valley(self):
        '''
        Algorithm to match the candidate list in valley order.
        It should be in descending order and ascending order, no other posibilities allowed.
        :return: Bool
        '''
        array = self.construct_permutation()
        start = array.index(self.minimum_value)

        array.reverse()
        end = len(array) - array.index(self.minimum_value)
        array.reverse()

        descend = array[ : start]
        constant = array[start : end]
        ascend = array[end : ]

        condition = self.issorted(descend, reverse=True) \
                    and self.issorted(ascend) \
                    and constant == self.minimum_array(end - start) \
                    and len(descend) \
                    and len(ascend)

        return condition

    def construct_permutation(self):
        '''
        Creates a solution list using generated positions and values provided in constructor
        :return: List
        '''
        permutation = []

        for elem in self.__permutation:
            permutation.append(self.__array[elem])

        return permutation

    @staticmethod
    def issorted(array, reverse=False):
        '''
        Checks if porivided list is sorted.
        Faster than sorted(list) == list
        :param array: List that should be checked
        :param reverse: Parameter for direction
        :return:
        '''
        for index in range(1, len(array)):
            if reverse and array[index - 1] < array[index]:
                return False
            elif not reverse and array[index - 1] > array[index]:
                return False
        return True

    def minimum_array(self, count):
        '''
        Generates an array with middle element in the lowest position of valley
        :param count: Number of minimum elements included
        :return:
        '''
        return [self.minimum_value] * count