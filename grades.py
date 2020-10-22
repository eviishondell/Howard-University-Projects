# Write a program which asks the user for student grades until the user types "done".
# The program should then compute the mean and median grades for all the students, rounded to two decimal places.
# See the instructions for further details.

def run():
    getting_input = True
    grades = []
    while getting_input:
        inp = input("Next grade: ")
        if inp == "done":
            getting_input = False
        else:
            grades.append(inp)

    grade_sum = 0
    for grade in grades:
        grade_sum += float(grade)
        total = grade_sum/len(grades)
        new_total = round(total, 2)
    print("Mean: " + str(new_total))

    new_list = []
    for i in grades:
        new_list.append(float(i))
    s = sorted(new_list)   
    if len(s) % 2 == 1:
        median = int((len(s) / 2))
        new_median = s[median]
        new = round(new_median , 2)
        print("Median: " + str(new))
    else:
        median = int((len(s) / 2))
        # print(median)
        ss = ((s[median]) + (s[median - 1])) / 2
        # print(float(new_list[median]))
        # print(float(new_list[median + 1]))
        # print(s)
        new_median = round(ss, 2)
        # print(new_median)
        print("Median: " + str(new_median))




if __name__ == "__main__":
    run()
