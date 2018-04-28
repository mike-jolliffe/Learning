class Books:

    def __init__(self, all_books, book_price, discount_dict):
        self.all_books = {'leftover': [], 'unused': all_books}
        self.num_books = len(all_books)
        self.book_price = book_price
        self.discount_dict = discount_dict
        self.best_discount_array = []
        self.discount_set = None
        self.book_sets = [[]]

    def find_per_book_discounts(self):
        """Return dictionary with discount key and book_set length value"""
        discount_length = {}
        for length, discount in self.discount_dict.items():
            discount_length.setdefault(discount / length,[]).append(length)
        return discount_length

    def order_discounts(self, discount_length):
        """Return sorted list of book_set lengths starting with best discount

        :param discount_length: An object that stores discounts by book_set length
        :type discount_length: dict
        :return: Modifies instance variables, returns nothing
        """
        keys_list = sorted([key for key in discount_length.keys()], reverse=True)
        for key in keys_list:
            self.best_discount_array.extend(sorted([value for value in discount_length[key]]))
        self.discount_set = self.best_discount_array[:]

    def make_set(self, set_size):
        """Move through all unused books, try to build book_set of set_size from them

        :param set_size: The length of book_set to build
        :type set_size: int
        """
        if self.all_books['unused']:
            book = self.all_books['unused'].pop()
            # Try to put the book in any available book_set
            for book_set in self.book_sets:
                if book not in book_set and len(book_set) < set_size:
                    book_set.append(book)
                    return self.make_set(set_size)
            # If book didn't go in book_set, move to used pile
            self.all_books['leftover'].append(book)
            return self.make_set(set_size)
        # Got through all unused books
        else:
            return None

    def total_cost(self):
        """Calculates total cost with discount applied
        :return: Returns total cost of all book_sets
        :rtype: float
        """
        total = 0.00
        #print(self.book_sets)
        for book_set in self.book_sets:
            try:
                discount = 1 - self.discount_dict[len(book_set)]
                total += discount * 8 * len(book_set)
            except KeyError:
                total += 8 * len(book_set)
        return total

    def main(self):
        # Calculate per-book discount
        per_book = self.find_per_book_discounts()
        # Sort array lengths best discount to worst
        self.order_discounts(per_book)
        # Pop array with best discount from front of 'queue'
        discount = self.best_discount_array.pop(0)
        # Build the first book_set
        self.make_set(discount)
        while True:
            # If any used books that didn't make it into a book_set
            if self.all_books['leftover']:
                # Move them back to unused pile
                self.all_books['unused'] = self.all_books['leftover']
                self.all_books['leftover'] = []
                # Add empty book_set and try again
                self.book_sets.append([])
                self.make_set(discount)
            # All books used
            else:
                try:
                    # Move onto next discount book_set size
                    discount = self.best_discount_array.pop(0)
                    # Create new unused list from all book_sets smaller than minimum book_set discount length
                    self.all_books['unused'] = [book for book_set in self.book_sets for book in book_set if len(book_set) not in self.discount_set]
                    book_set_copy = self.book_sets[:]
                    # Remove for rebuild all book_sets smaller than minimum discount length
                    for book_set in book_set_copy:
                        if len(book_set) not in self.discount_set:
                            self.book_sets.remove(book_set)
                    self.make_set(discount)
                # All discounts applied
                except:
                    cost = self.total_cost()
                    return (f"\nBooksets: {self.book_sets} \n Cost: ${cost: .2f}\n")


if __name__ == '__main__':

    # Example we worked through
    inventory1 = Books([1, 2, 3, 4, 2, 3, 4, 5], 8, {3: 0.10, 4: 0.20, 5: 0.25})
    print("-------------------------------------")
    print("Example provided in problem specs")
    print(inventory1.main())
    print("A 5-book and 3-book set, instead:")
    print(f"${3*8*.90 + 5*8*.75: .2f}")
    print("-------------------------------------")

    # Handle all same books
    print("-------------------------------------")
    inventory2 = Books([1,1,1,1,1,1,1,1,1], 8, {3: 0.10, 4: 0.20, 5: 0.25})
    print("Handle a bunch of one_book sets")
    print(inventory2.main())
    print("-------------------------------------")

    # Build different sets based on best discounts
    # Should build lots of three-book sets
    print("-------------------------------------")
    inventory3 = Books([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,1,2,3,4,5,6], 8, {3: 0.10, 6: 0.15, 9: 0.10})
    print("Should build three-book sets and six book sets to get best discount")
    print(inventory3.main())

    # Same books but should build a bunch of nine-book sets
    inventory4 = Books([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,1,2,3,4,5,6], 8, {3: 0.10, 6: 0.30, 9: 0.70})
    print("Same books, different discount: should build nine-book sets, six book sets, and three book sets for the better discount")
    print(inventory4.main())
    print("-------------------------------------")
