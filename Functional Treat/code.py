data_summary={}

def get_input():
    global data_summary
    print("\n Enter data for a array : ")
    user_input = input().split()
    data = [int(i) for i in user_input]
    data_summary['total_elements'] = len(data)
    print("Data has been stored successfully!")
    return data

def display(data):
    if not data:
        print("No data available ")
        return
    

    print("\nData Summary:")
    print(f"- Total elements: {len(data)}")
    print(f"- Minimum value: {min(data)}")
    print(f"- Maximum value: {max(data)}")
    print(f"- Sum of all values: {sum(data)}")
    print(f"- Average value: {sum(data)/len(data)}")

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

def filter_data(data):
    a = int(input("\nfilter data "))
    b = list(filter(lambda x: x >= a, data))
    print(f"Filtered Data (values >= {a}):")
    print(", ".join(map(str, b)))

def sort(data) :
    print("\nselect option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter you select : ")

    temp_data = data.copy()
    if choice == "1" or choice=="01":
        temp_data.sort()
        print(f"Sorted Data in Ascending: {temp_data}")
    else:
        temp_data.sort(reverse=True)
        print(f"Sorted Data in Descending : {temp_data}")   


def info(data):
    if not data: 
        return 0, 0, 0, 0
    s = sum(data)
    mi = min(data)
    ma = max(data)
    avg = s / len(data)
    return mi, ma, s, avg



def data_info(**kwargs):
    print("\nDataset Statistics:")
    for key, value in kwargs.items():
        print(f"- {key.replace('_', ' ').capitalize()}: {value}")


def main_menu():
    dataset = [] 




    while True:
        print("\nWelcome to the Data Analyzer  ---")
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary")
        print("3. Calculate Factorial ")
        print("4. Filter Data")
        print("5. Sort Data")
        print("6. Display Statistics ")
        print("7. Exit Program")
        
        choice = input("Please enter your choice: ")
        
        if choice == "1" or choice=="01":
            dataset = get_input()
        elif choice == "2" or choice=="02":
            display(dataset)
        elif choice == "3" or choice=="03":
            num = int(input("Enter a number calculate factorial: "))
            print(f"Factorial of {num} is: {fact(num)}")
        elif choice == "4" or choice=="04":
            if dataset: filter_data(dataset)
            else: print("Please input data first!")
        elif choice == "5" or choice=="05":
            if dataset: sort(dataset)
            else: print("Please input data first!")
        elif choice == "6" or choice=="06":
            if dataset:
                mi, ma, s, avg = info(dataset)
              
                data_info(minimum_value=mi, maximum_value=ma, sum_of_all_values=s, average_value=round(avg, 2))
            else:
                print("Please input data first!")
        elif choice == "7" or choice=="07":
            print("Thank you for using the Data Analyzer . Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()


