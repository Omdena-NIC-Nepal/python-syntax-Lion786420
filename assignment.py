def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number>10:
        return "Greater"
    elif number<10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum=0
    for each_number in range(1,n+1):
        sum+=each_number
    return sum

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    sum=0
    max=numbers[0]
    min=numbers[0]
    for number in numbers:
        sum+=number
        if number>max:
            max=number
        if number<min:
            min=number
    return (sum,max,min)
        

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    student_list=[]
    for student_detail in students_dict:
        if students_dict[student_detail]>80:
            student_list.append(student_detail)
    return student_list

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements=set()
    for item in list1:
        if item in list2:
            common_elements.add(item)
    return common_elements
        

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {"sum":a+b,"difference":a-b,"product":a*b,"quotient":a/b}

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {"and":x and y,"or":x or y,"not_x":not x}

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {"and":a & b,"or":a | b,"xor":a ^ b}