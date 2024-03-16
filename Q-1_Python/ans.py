"""Name : Ved Lakkad
Enrollment No. : 2302031700019
ID : 8118
Phone number : 9974876307
Question : 1"""


def create_lists():
    # creating list
    num_elements1 = int(input("Enter the number of elements for list 1: "))
    num_elements2 = int(input("Enter the number of elements for list 2: "))

    list1 = []
    list2 = []

    print("Enter elements for list 1:")
    for i in range(num_elements1):
        element = int(input(f"Element {i+1}: "))
        list1.append(element)

    print("Enter elements for list 2:")
    for i in range(num_elements2):
        element = int(input(f"Element {i+1}: "))
        list2.append(element)

    return list1, list2


# list ne numbers ma bdalva
def list_to_number(list1):
    number = int("".join(map(str, list1)))
    return number


# numver thi list
def number_to_list(number):
    list1 = [int(digit) for digit in str(number)]
    return list1


def main():
    list1, list2 = create_lists()

    # List to number conversion
    number1 = list_to_number(list1)
    number2 = list_to_number(list2)
    print("Numbers from lists:", number1, number2)

    # Addition and multiplication
    sum_number = number1 + number2
    product_number = number1 * number2
    print("Sum:", sum_number)
    print("Product:", product_number)

    # Number to list conversion
    sum_list = number_to_list(sum_number)
    product_list = number_to_list(product_number)
    print("Sum as list:", sum_list)
    print("Product as list:", product_list)


if __name__ == "__main__":
    main()
