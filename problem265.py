import numpy as np

def main():
    circle = BinaryCircle(32, 5)
    sum = compute_sequences(circle, 5)
    print(sum)

class BinaryCircle:
    def __init__(self, size: int, seq_size: int):
        """Generates a Binary Circle of given size, where the sequence size should be log2(size)"""
        self.size = size
        self.circle = np.zeros(size + seq_size - 1)
        self.seq_size = seq_size
        self.sequences = {sum_sequence(self.circle[:seq_size])}
    
    def get_sequence_from_circle(self, index: int):
        """returns a sequence (ending at given index) of length N"""
        return self.circle[index - self.seq_size+1:index+1]

    def set_value(self, index: int, value: bool):
        """sets a value at the desired index on the circle"""
        if (index < self.seq_size):
            raise Exception("forbidden value for index")
        else:
            self.circle[index] = value
            self.sequences.add(sum_sequence(self.circle[index - self.seq_size+1:index+1]))
    
    def check_value(self, index: int, value: bool):
        """checks whether setting a bit generates a new or an already present subsequence"""
        seq = self.get_sequence_from_circle(index)
        seq[-1] = value
        return sum_sequence(seq) not in self.sequences
    
def sum_sequence(seq):
    """returns the value of the sequence interpreted as binary, with the BinaryCircle.seq_size zeros as the MSBs"""
    sum = 0
    for i in range(len(seq)):
        sum += seq[len(seq)-i-1] * 2**i
    return sum


def compute_sequences(circle: BinaryCircle, index: int):
    """recursively computes all possibilities of sequences, returns the binary sum when the sequence is complete or 0 if the sequence is not possible to finish"""
    if(index == len(circle.circle)):
        return sum_sequence(circle.circle[:circle.size])
    new_index = index + 1
    
    check_zero = circle.check_value(index, 0)
    if(index < circle.size):
        check_one = circle.check_value(index, 1)
    else:
        check_one = False

    circle_zero = BinaryCircle(circle.size, circle.seq_size)
    if(check_zero):
        circle_zero.circle = circle.circle.copy()
        circle_zero.sequences = circle.sequences.copy()
        if (index < circle_zero.size):
            circle_zero.set_value(index, 0)

    circle_one = BinaryCircle(circle.size, circle.seq_size)
    if(check_one):
        circle_one.circle = circle.circle.copy()
        circle_one.sequences = circle.sequences.copy()
        if (index < circle_one.size):
            circle_one.set_value(index, 1)

    if(check_zero and check_one):
        return compute_sequences(circle_zero, new_index) + compute_sequences(circle_one, new_index)
    elif(check_zero):
        return compute_sequences(circle_zero, new_index)
    elif(check_one):
        return compute_sequences(circle_one, new_index)
    else:
        return 0

if __name__ == "__main__":
    main()