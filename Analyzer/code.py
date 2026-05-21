import numpy as np

class DataAnalytics:

    def __init__(self):
        self.data = None 

    def create_array(self):
        print("\n Create Array")
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        elements = list(map(float, input(f"Enter {rows*cols} elements: ").split()))
        
        self.data = np.array(elements).reshape(rows, cols)
        
        print("\nArray Created:")
        print(self.data)

    def math_operations(self):
        print("\n--- Math Operations ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = input("Enter choice: ")
        
        elements = list(map(float, input("Enter elements for second array: ").split()))
        other = np.array(elements).reshape(self.data.shape)

        if choice == '1':
            result = self.data + other
        elif choice == '2':
            result = self.data - other
        elif choice == '3':
            result = self.data * other
        elif choice == '4':
            result = self.data / other
        else:
            print("Invalid choice")
            return

        print("\nResult:")
        print(result)

    def combine_array(self):
        print("\nCombine Arrays")
        
        elements = list(map(float, input("Enter elements for second array: ").split()))
        other = np.array(elements).reshape(self.data.shape)

        result = np.vstack((self.data, other))

        print("\nCombined Array:")
        print(result)

    def search_sort_filter(self):
        print("\nSearch  Sort  Filter ---")
        print("1. Search")
        print("2. Sort")
        print("3. Filter")
        
        choice = input("Enter choice: ")

        if choice == '1':
            value = float(input("Enter value to search: "))
            a = np.where(self.data == value)
            print("Found at index:",a)

        elif choice == '2':
            sorted_data = np.sort(self.data, axis=None).reshape(self.data.shape)
            print("Sorted Array:")
            print(sorted_data)

        elif choice == '3':
            limit = float(input("Enter limit: "))
            filtered = self.data[self.data > limit]
            print("Filtered Values:", filtered)

        else:
            print("Invalid choice")

    def statistics(self):
        print("\n Statistics ")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = input("Enter choice: ")

        if choice == '1':
            print("Sum:", np.sum(self.data))
        elif choice == '2':
            print("Mean:", np.mean(self.data))
        elif choice == '3':
            print("Median:", np.median(self.data))
        elif choice == '4':
            print("Std Dev:", np.std(self.data))
        elif choice == '5':
            print("Variance:", np.var(self.data))
        else:
            print("Invalid choice")



def main():
    obj = DataAnalytics()

    while True:
        print("\n MENU ")
        print("1. Create Array")
        print("2. Math Operations")
        print("3. Combine Arrays")
        print("4. Search / Sort / Filter")
        print("5. Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            obj.create_array()

        elif choice == '2':
            if obj.data is not None:
                obj.math_operations()
            else:
                print(" create array")

        elif choice == '3':
            if obj.data is not None:
                obj.combine_array()
            else:
                print(" create array")

        elif choice == '4':
            if obj.data is not None:
                obj.search_sort_filter()
            else:
                print(" create array")

        elif choice == '5':
            if obj.data is not None:
                obj.statistics()
            else:
                print(" create array ")

        elif choice == '6':
            print("Program End")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
