""" PBC 110-1 TA_interview question 3"""

class Best_location:
    """A class used to get best location
    Attrs:
    ---
        town_number: int
            a formatted string to print out what the animal says
        town_info: Dict{
            'fire': List[int],
                The number of times a town caught in the fire
            'distance': List[List[int]],
                Record distance between the town itself and others
            'expected_distance': List[int],
                Weighted distance with fire
        }
        best: tuple
            self.best = (best_town_location, min_expected_distance)

    Methods:
    ---
        update
            take inputs and call self.get_best_location()
        get_best_location
            calculate weighted distance and find the best location
    """

    def __init__(self):
        self.town_number = int()
        self.town_info = {
            'fire': list(),
            'distance': list(),
            'expected_distance': list(),}
        self.best = tuple()
    
    def update(self):
        self.town_number = int(input())
        fire_list = [int(i) for i in input().split(',')]
        for i in range(self.town_number):
            self.town_info['fire'].append(fire_list[i])
            self.town_info['distance'].append([int(j) for j in input().split(',')])
        self.best = self.get_best_location()
    
    def get_best_location(self):
        for i in range(self.town_number):
            expected_distance = 0
            for j in range(self.town_number):
                expected_distance += self.town_info['fire'][j] * \
                    self.town_info['distance'][i][j]
            self.town_info['expected_distance'].append(expected_distance)

        return (self.town_info['expected_distance'].index(
            min(self.town_info['expected_distance'])) + 1,
            min(self.town_info['expected_distance']))


best_location = Best_location()
best_location.update()
print(best_location.best)
# print(vars(best_location))