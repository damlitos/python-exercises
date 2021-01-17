class MovingTotal:

    def append(self, numbers):
        numbers.append(self)

        pass

    def find_len(self):
        print(len(self))


    def contains(self, total):

        return None


if __name__ == "__main__":
    movingtotal =  MovingTotal()
    movingtotal.append((1,2,3))
    print(movingtotal.find_len())