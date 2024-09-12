def determine_drink_grades(known_drinks, drinks_to_grade):
    # Known drinks dictionary
    drink_dict = {}
    for drink, grade in known_drinks:
        drink_dict[drink] = grade

    # Determine grades for drinks to grade
    results = []
    for drink in drinks_to_grade:
        if drink in drink_dict:
            results.append(drink_dict[drink])
        else:
            # Attempt to split the drink name into parts and determine the grade
            grade = ""
            temp_drink = drink
            for i in range(len(temp_drink)):
                for part in drink_dict:
                    if temp_drink.startswith(part):
                        grade += drink_dict[part]
                        temp_drink = temp_drink[len(part):]
                        break
            if temp_drink:  # If there are leftover parts that don't match
                grade = "D"  # Default grade if not all parts are known
            results.append(grade)

    return results

def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    # Read the first line
    N, M = map(int, data[0].split())
    
    # Read known drinks and their grades
    known_drinks = []
    for i in range(1, N + 1):
        parts = data[i].split()
        known_drinks.append((parts[0], parts[1]))
    
    # Read drinks to grade
    drinks_to_grade = []
    for i in range(N + 1, N + 1 + M):
        drinks_to_grade.append(data[i])
    
    return known_drinks, drinks_to_grade

# Main function to execute the grading process
def main():
    known_drinks, drinks_to_grade = read_input()
    grades = determine_drink_grades(known_drinks, drinks_to_grade)
    
    for grade in grades:
        print(grade)

if __name__ == "__main__":
    main()
