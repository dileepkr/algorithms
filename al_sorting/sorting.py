class Sorting:
    def __init__(self, sort_function) -> None:
        self.sort = getattr(Sorting, sort_function)
    
    def bubble_sort(self, list_to_sort) -> list:
        '''
        Bubble up the max value to the correct location in each pass
        '''
        for i in range(len(list_to_sort)):
            ptr1 = 0
            ptr2 = 1
            while ptr2 < len(list_to_sort)-i:
                if list_to_sort[ptr1] > list_to_sort[ptr2]:
                    temp = list_to_sort[ptr1]
                    list_to_sort[ptr1] = list_to_sort[ptr2]
                    list_to_sort[ptr2] = temp
                ptr1 += 1
                ptr2 += 1
        return list_to_sort
    
    def selection_sort(self, list_to_sort):
        """
        Identify the largest value in each pass and swap it with the correct spot
        Pros:
        This sorting takes significantly lesser number of swaps compared to bubble sort
        """
        for _pass in range(len(list_to_sort)-1, -1, -1):
            largest_ptr = 0
            for index in range(_pass+1):
                if list_to_sort[index] > list_to_sort[largest_ptr]:
                    largest_ptr = index
            list_to_sort[largest_ptr], list_to_sort[_pass] = list_to_sort[_pass], list_to_sort[largest_ptr]
        return list_to_sort

    def insertion_sort(self, list_to_sort):
        '''
        Maintain a list of sorted elements starting at index 0
        As we proceed down the list, insert the element into it's correct position in the sorted list
        Pros:
        Since shifting is faster than swapping, insertion sort performs faster
        '''
        for pass_ptr in range(1, len(list_to_sort)):
            item_to_sort = list_to_sort[pass_ptr]
            # for sorted_list_ptr in range(pass_ptr-1, -1, -1):
            #     if item_to_sort < list_to_sort[sorted_list_ptr]:
            #         list_to_sort[sorted_list_ptr+1] = list_to_sort[sorted_list_ptr]
            #         list_to_sort[sorted_list_ptr] = item_to_sort
            #     else:
            #         break
            position = pass_ptr
            while position > 0 and list_to_sort[position-1] > item_to_sort:
                list_to_sort[position] = list_to_sort[position-1]
                position = position-1
            list_to_sort[position] = item_to_sort
        return list_to_sort

    def shell_sort(self, list_to_sort):
        
        pass

    def merge_sort(self, list_to_sort):
        pass

    def quick_sort(self, list_to_sort):
        pass

if __name__ == "__main__":
    s = Sorting("bubble_sort")
    print(s.bubble_sort([5,1,56,4,34,13,2,285,1]))
    print(s.selection_sort([5,1,56,4,34,13,2,285,1]))
    print(s.insertion_sort([5,1,56,4,34,13,2,285,1]))