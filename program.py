# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution.

# Student ID: w1867616

# Date: 06/12/2021

# part4
credit_numbers = [0, 10, 20, 40, 60, 80, 100, 120]
pass_credits = 0
defer_credits = 0
fail_credits = 0
total_credits = 0


total_progress = 0
total_trailer = 0
total_retriever = 0
total_exclude = 0
total_outcomes = 0
progress_outcome = ""

list_results = []
count1 = 0


def validation_student():
    """Check input value type, value range, and
     if the total credits = 120."""

    global pass_credits, defer_credits, fail_credits, total_credits
    while total_credits != 120:
        try:
            pass_credits = int(input('Pleas enter your credit at pass: '))
            if pass_credits not in credit_numbers:
                print("Out of range\n")
                continue

            defer_credits = int(input('Pleas enter your credit at defer: '))
            if defer_credits not in credit_numbers:
                print("Out of range\n")
                continue

            fail_credits = int(input('Pleas enter your credit at fail: '))
            if fail_credits not in credit_numbers:
                print("Out of range\n")
                continue

        except ValueError:
            print("Integer Required\n")

        else:
            total_credits = pass_credits + defer_credits + fail_credits

            if total_credits != 120:
                print(end='' "Total incorrect\n\n")

            else:
                continue


def validation_staff():
    """Check input value type, value range, and
         if the total credits = 120."""

    global pass_credits, defer_credits, fail_credits, total_credits
    while total_credits != 120:
        try:
            pass_credits = int(input('Enter your total PASS credits: '))
            if pass_credits not in credit_numbers:
                print("Out of range\n")
                continue

            defer_credits = int(input('Enter your total DEFER credits: '))
            if defer_credits not in credit_numbers:
                print("Out of range\n")
                continue

            fail_credits = int(input('Enter your total FAIL credits: '))
            if fail_credits not in credit_numbers:
                print("Out of range\n")
                continue

        except ValueError:
            print("Integer Required\n")

        else:
            total_credits = pass_credits + defer_credits + fail_credits

            if total_credits != 120:
                print(end='' "Total incorrect\n\n")

            else:
                continue


def outcome():
    """Check the credits points and
     find the correct progression outcome"""
    global progress_outcome
    if pass_credits == 120:
        progress_outcome = "Progress"
        print(progress_outcome)

    elif pass_credits == 100:
        progress_outcome = "Progress (module trailer)"
        print(progress_outcome)

    elif pass_credits == 80:
        progress_outcome = "Module retriever"
        print(progress_outcome)

    elif pass_credits == 60:
        progress_outcome = "Module retriever"
        print(progress_outcome)

    elif pass_credits == 40:

        if defer_credits == 0 and fail_credits == 80:
            progress_outcome = "Exclude"
            print(progress_outcome)

        else:
            progress_outcome = "Module retriever"
            print(progress_outcome)

    elif pass_credits == 20:

        if defer_credits == 20 and fail_credits == 80:
            progress_outcome = "Exclude"
            print(progress_outcome)

        elif defer_credits == 0 and fail_credits == 100:
            progress_outcome = "Exclude"
            print(progress_outcome)

        else:
            progress_outcome = "Module retriever"
            print(progress_outcome)

    elif pass_credits == 0:
        if defer_credits == 40 and fail_credits == 80:
            progress_outcome = "Exclude"
            print(progress_outcome)

        elif defer_credits == 20 and fail_credits == 100:
            progress_outcome = "Exclude"
            print(progress_outcome)

        elif defer_credits == 0 and fail_credits == 120:
            progress_outcome = "Exclude"
            print(progress_outcome)

        else:
            progress_outcome = "Module retriever"
            print(progress_outcome)

    else:
        print("something went wrong")


def horizontal_histogram():
    global total_outcomes
    print('Horizontal Histogram')

    print("Progress {}  : ".format(total_progress), end='')
    for i in range(total_progress):
        print("*", end=' ')

    print("\nTrailer {}   : ".format(total_trailer), end='')
    for i in range(total_trailer):
        print("*", end=' ')

    print("\nRetriever {} : ".format(total_retriever), end='')
    for i in range(total_retriever):
        print("*", end=' ')

    print("\nExcluded {}  : ".format(total_exclude), end='')
    for i in range(total_exclude):
        print("*", end=' ')
    print()


def vertical_histogram():
    print('Vertical Histogram')
    print(f"Progress {total_progress}|Trailer {total_trailer}|Retriever {total_retriever}|Excluded {total_exclude}")

    a = '   *'

    list_vertical = [[], [], [], []]

    for i in range(total_progress):
        list_vertical[0].append(a)
    for j in range(total_trailer):
        list_vertical[1].append(a)
    for k in range(total_retriever):
        list_vertical[2].append(a)
    for m in range(total_exclude):
        list_vertical[3].append(a)

    maximum = max(total_progress, total_trailer, total_retriever, total_exclude)

    if len(list_vertical[0]) != maximum:
        for i in range(maximum - len(list_vertical[0])):
            list_vertical[0].append('')
    if len(list_vertical[1]) != maximum:
        for j in range(maximum - len(list_vertical[1])):
            list_vertical[1].append('')
    if len(list_vertical[2]) != maximum:
        for k in range(maximum - len(list_vertical[2])):
            list_vertical[2].append('')
    if len(list_vertical[3]) != maximum:
        for m in range(maximum - len(list_vertical[3])):
            list_vertical[3].append('')

    for x in range(maximum):
        print('%-10s %-10s %-10s %s' % (list_vertical[0][x], list_vertical[1][x], list_vertical[2][x], list_vertical[3][x]))


def outcome_list():
    global count1, list_results
    for i in range(count1, count1 + 1):           # https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
        list_results.append([])

        list_results[i].append(progress_outcome)
        list_results[i].append(pass_credits)
        list_results[i].append(defer_credits)
        list_results[i].append(fail_credits)

    count1 += 1


def outcome_txt_file():
    f1 = open('outcome_file.txt', 'a')
    f1.write(f"\n{progress_outcome} - {pass_credits}, {defer_credits}, {fail_credits}")

    f1.close()


def staff_check_text_file():
    """This function for staffs to
    check the students outcomes"""

    print("Staff Version with Text file(extension: part4)")
    global pass_credits, defer_credits, fail_credits, total_credits, credit_numbers
    global total_progress, total_trailer, total_retriever, total_exclude, total_outcomes, count1
    option = 'y'
    while option != 'q':

        # check input value type, range and total credits
        validation_staff()

        # find and Display the outcomes
        outcome()

        # save the progress type and credits points into a nested list
        outcome_list()

        # insert the progress type and credits points into a Text File
        outcome_txt_file()

        # counting different progress outcomes
        if progress_outcome == "Progress":
            total_progress += 1

        elif progress_outcome == "Progress (module trailer)":
            total_trailer += 1

        elif progress_outcome == "Module retriever":
            total_retriever += 1

        elif progress_outcome == "Exclude":
            total_exclude += 1

        total_credits = 0
        # asking for continue or stop
        print('\nWould you like to enter another set of data?')
        while True:
            option = input("Enter 'y' for yes or 'q' to quit and view results:")
            if option == 'y' or option == 'q':
                break

            else:
                print("wrong input")

        print()
    print("-------------------------------------------------------------------------------")

    # Horizontal Histogram
    horizontal_histogram()

    print("-------------------------------------------------------------------------------")

    # Vertical Histogram
    vertical_histogram()

    print("\n-------------------------------------------------------------------------------")

    # print the data stored in the list_credits.........................................................................
    print('Progression Outcome List\n')
    for j in range(count1):
        print("{} - {}, {}, {}".format(list_results[j][0], list_results[j][1], list_results[j][2], list_results[j][3]))

    print("-------------------------------------------------------------------------------")

    # print the data stored in the Text file (out_txt_file).
    print('Progression Outcome Text file')
    f3 = open('outcome_file.txt', 'r')
    data = f3.read()
    f3.close()
    print(data)

    total_outcomes = total_progress + total_trailer + total_retriever + total_exclude
    print('\n{} outcomes in total.'.format(total_outcomes))
    print("-------------------------------------------------------------------------------")


def menu():
    global total_credits, total_progress, total_trailer, total_retriever, total_exclude, total_outcomes
    global count1, list_results
    while True:
        print("\n")

        try:
            menu_option = input("Enter '1' to Open Students Version\n"
                                "Enter '2' to Open Staff Version\n"
                                "Enter 'q' to Quit\n"
                                "\nEnter Option Number:")
            print("\n")
        except ValueError:
            print("Please Enter '1' '2' or 'q'")
        else:
            if menu_option == "1":
                validation_student()

                outcome()

            elif menu_option == "2":
                staff_check_text_file()

            elif menu_option == "q":
                break

            else:
                print("Please Enter '1', '2', 'q'")

        total_credits = 0
        total_progress = 0
        total_trailer = 0
        total_retriever = 0
        total_exclude = 0
        total_outcomes = 0

        count1 = 0

        list_results.clear()

        f = open('outcome_file.txt', 'w')
        f.close()

menu()
