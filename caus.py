
class MovingTotal:

     # init method or constructor 
    def __init__(self): 
        self.elts = []
        self.len = 0
        
        
    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        
        self.elts = self.elts.append(numbers)
        self.len = len(self.elts)
        
        pass
    
    def find_len(self):
        
        return self.len
    

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        elts = self.elts
        
        for i in range(0, len(elts)-2):
            if total== np.sum(elts[i:i+3]):
                return True
        
        return False
    
    
if __name__ == "__main__":
    
    movingtotal = MovingTotal()
    movingtotal.append([1, 2, 3])
    print(movingtotal.find_len())
    
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    movingtotal.append([4])
    print(movingtotal.contains(9))