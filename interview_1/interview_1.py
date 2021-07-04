""" PBC 110-1 TA_interview question 1"""

class Classifer:
    """identify whether the content is written by male or female"""

    def __init__(self):
        self.training_size = 0
        self.validating_size = 0
        self.training_set = list()
        self.validating_set = list()
        self.avg_upper_bound = 0
        self.critical_value = None
        self.error_term = 0
        self.GENDER = 0
        self.AVG_LEN = 1
    
    def update(self):
        self.training_size, self.validating_size = [int(i) for i in input().split(',')]
        for i in range(self.training_size):
            temp = input()
            avg_sentence_len = self.calculate_sentence_len_avg(temp[2:])

            # update avg_upper_bound
            if avg_sentence_len > self.avg_upper_bound:
                self.avg_upper_bound = int(avg_sentence_len + 1)
            self.training_set.append([int(temp[0]), avg_sentence_len])
        for i in range(self.validating_size):
            temp = input()
            avg_sentence_len = self.calculate_sentence_len_avg(temp[2:])
            self.validating_set.append([int(temp[0]), avg_sentence_len])
        # print(self.training_set)
        # print(self.validating_set)
    
    def calculate_sentence_len_avg(self, process_section):
        # preserve '.' inside float
        for deli in ['.', ',']:
            index = 0
            while True:
                index = process_section.find(deli, index + 1)
                if index == -1:
                    break
                elif ((index - 1 >= 0) and (index + 1 < len(process_section)) and 
                        process_section[index-1].isdigit() and 
                        process_section[index+1].isdigit()):
                    process_section = process_section[:index] + '*' + process_section[index+1:]

        # trimming str and calculate the avg
        for word_seg in ['.', ';', ':', '!', '?']:  # replace words that need to be segmentated
            process_section = process_section.replace(word_seg, ',')    

        # split str by ',' and remove empty str
        process_section = list(filter(None, process_section.strip().split(',')))

        # remove space at the beginning and start for each sentence
        process_section = [j.strip() for j in process_section]
        return sum(len(j.split(' ')) for j in process_section) / len(process_section)
    
    def train(self):
        # traverse through all possible critical point
        correctness_list = []
        for value in range(self.avg_upper_bound + 1):
            correctness = 0
            for each in self.training_set:
                # female
                if (each[self.AVG_LEN] >= value and
                        each[self.GENDER] == 2):
                    correctness += 1
                # male
                elif (each[self.AVG_LEN] < value and
                        each[self.GENDER] == 1):
                    correctness += 1
            correctness_list.append(correctness)
        
        self.critical_value = correctness_list.index(max(correctness_list))
        return self.critical_value
    
    def validate(self):
        # check if self.train() has been executed
        if not self.critical_value:
            self.train()
        
        for each in self.validating_set:
            # female
            if (each[self.AVG_LEN] >= self.critical_value and
                    each[self.GENDER] != 2):
                self.error_term += 1
            # male
            elif (each[self.AVG_LEN] < self.critical_value and
                    each[self.GENDER] != 1):
                self.error_term += 1
        return self.error_term

classifer = Classifer()
classifer.update()
print(f'{classifer.train()},{classifer.validate()}')