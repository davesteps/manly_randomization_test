import numpy as np

class RandomizationTest:
    def __init__(self, group1: np.array, group2: np.array, iterations: int = 1e5):
        self.group1 = group1
        self.group2 = group2
        self.group1_n = len(group1)
        self.group2_n = len(group2)
        self.combined = np.concatenate((group1, group2))
        self.iterations = iterations

    def observed_difference(self):
        return np.mean(self.group1) - np.mean(self.group2)

    def shuffle(self):
        np.random.shuffle(self.combined)
        return self.combined[:self.group1_n], self.combined[self.group1_n:]

    def test(self):
        observed_difference = self.observed_difference()
        count = 0

        for _ in range(self.iterations):
            group1, group2 = self.shuffle()
            if abs(np.mean(group1) - np.mean(group2)) >= abs(observed_difference):
                count += 1

        return count / self.iterations

