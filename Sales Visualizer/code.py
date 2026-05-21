import pandas as pd
import matplotlib.pyplot as plt

class SalesAnalyzer:

    def __init__(self):
        self.data = None

    def load_data(self, path):
        try:
            self.data = pd.read_csv(path)
            print("\nData loaded successfully!")
        except Exception as e:
            print("Error:", e)


    def show_data(self):
        if self.data is not None:
            print(self.data.head())
        else:
            print("No data found!")


    def show_info(self):
        if self.data is not None:
            print(self.data.info())
        else:
            print("No data!")


    def show_stats(self):
        if self.data is not None:
            print(self.data.describe())
        else:
            print("No data!")


    def handle_missing(self):
        if self.data is not None:
            print("Missing values:\n", self.data.isnull().sum())
            self.data = self.data.fillna(0)
            print("Missing values filled with 0")
        else:
            print("No data!")

    def sort_data(self, column):
        if self.data is not None:
            print(self.data.sort_values(by=column))
        else:
            print("No data!")


    def filter_data(self, column, value):
        if self.data is not None:
            print(self.data[self.data[column] == value])
        else:
            print("No data!")


    def calculate(self, column):
        if self.data is not None:
            print("Sum:", self.data[column].sum())
            print("Mean:", self.data[column].mean())
        else:
            print("No data!")


    def plot_data(self, column):
        if self.data is not None:
            self.data[column].plot(kind='bar')
            plt.title("Bar Chart")
            plt.show()
        else:
            print("No data!")



def main():
    obj = SalesAnalyzer()

    while True:
        print("\n==== Data Analysis Menu ====")
        print("1. Load Data")
        print("2. Show Data")
        print("3. Show Info")
        print("4. Show Statistics")
        print("5. Handle Missing Values")
        print("6. Sort Data")
        print("7. Filter Data")
        print("8. Calculate Sum & Mean")
        print("9. Plot Data")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            path = input("Enter CSV file path: ")
            obj.load_data(path)

        elif choice == '2':
            obj.show_data()

        elif choice == '3':
            obj.show_info()

        elif choice == '4':
            obj.show_stats()

        elif choice == '5':
            obj.handle_missing()

        elif choice == '6':
            col = input("Enter column name: ")
            obj.sort_data(col)

        elif choice == '7':
            col = input("Enter column name: ")
            val = input("Enter value: ")
            obj.filter_data(col, val)

        elif choice == '8':
            col = input("Enter column name: ")
            obj.calculate(col)

        elif choice == '9':
            col = input("Enter column name: ")
            obj.plot_data(col)

        elif choice == '10':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
