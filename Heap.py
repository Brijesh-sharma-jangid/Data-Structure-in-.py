def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


class Minheap:
    def __init__(self):
        self.H = [None]

    def top(self):
        return self.H[1]

    def __repr__(self):
        return str(self.H[1:])

    def bubble_up(self, i):
        if i <= 1:
            return
        else:
            if self.H[i] <= self.H[i // 2]:
                self.H[i], self.H[i // 2] = self.H[i // 2], self.H[i]
                self.bubble_up(i // 2)
            return

    def bubble_down(self, i):
        if left(i) > len(self.H):
            return
        if left(i) <= len(self.H) < right(i):
            if self.H[i] > self.H[left(i)]:
                self.H[i], self.H[left(i)] = self.H[left(i)], self.H[i]
                self.bubble_down(left(i))
        else:
            min_child_value, min_child_index = min((self.H[left(i)], left(i)), (self.H[right(i)], right(i)))
            self.H[i], self.H[min_child_index] = self.H[min_child_index], self.H[i]
            self.bubble_down(min_child_index)
        return

    def insert(self, elt):
        self.H.append(elt)
        self.bubble_up(len(self.H) - 1)

    def delete(self):
        self.H[1], self.H[len(self.H) - 1] = self.H[len(self.H) - 1], self.H[1]
        self.H.pop()
        self.bubble_down(1)


if __name__ == '__main__':
    Q = Minheap()
    Q.insert(5)
    Q.insert(2)
    Q.insert(4)
    Q.insert(-1)
    Q.insert(7)
    print(repr(Q))
