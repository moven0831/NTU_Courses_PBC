""" PBC 110-1 TA_interview question 2"""

class Best_prediction:
    def __init__(self):
        self.eigenvalues_number = int()
        self.stock_number = int()
        self.eigenvalues_matrix = list()
        self.analysis_table = {
            'predicted_bar': list(),    # (stock, value, direction)
            'prediction': list(),       # direction: -1 for down, 1 for up
            'total_error': list(),}

    def update(self):
        self.eigenvalues_number = int(input())
        self.stock_number = int(input())
        for i in range(self.stock_number):
            self.eigenvalues_matrix.append([int(j) for j in input().split(',')])
        self.create_prediction_table()
            

    def create_prediction_table(self):
        for value in range(self.eigenvalues_number):
            for stock_i in range(self.stock_number):
                self.analyse(value=value, stock=stock_i, direction=1)
                self.analyse(value=value, stock=stock_i, direction=-1)

    def analyse(self, value, stock, direction):
        self.analysis_table['predicted_bar'].append((value, self.eigenvalues_matrix[stock][value], direction))
        current_prediction = list()
        for each in range(self.stock_number):
            if (self.eigenvalues_matrix[each][value] >= self.eigenvalues_matrix[stock][value] and
                    self.eigenvalues_matrix[each][-1] == direction):
                current_prediction.append(True)
            elif (self.eigenvalues_matrix[each][value] < self.eigenvalues_matrix[stock][value] and
                    self.eigenvalues_matrix[each][-1] == -direction):
                current_prediction.append(True)
            else:
                current_prediction.append(False)
        self.analysis_table['prediction'].append(current_prediction)
        self.analysis_table['total_error'].append(current_prediction.count(False))
    

prediction = Best_prediction()
prediction.update()
print(min(prediction.analysis_table['total_error']))
# print(vars(prediction))