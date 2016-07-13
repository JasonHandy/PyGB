#!/usr/local/bin/python3
import os
import ExportXML
import ParseXML
import EditXML
import ErrorHandler
import Statistics

# TODO: Make name entry more fluid (no pressing enter)
def open_file():
    total_books = 0
    gradebook_string = ""

    # Return xml files found in documents folder
    for gradebook in os.listdir(save_path):
        if gradebook.endswith('.xml'):
            total_books += 1
            gradebook_string += "> {!s}\n".format(gradebook.replace('.xml', ''))

    # Prompt user to create new grade book if no grade book exists
    if total_books == 0:
        print("Looks like you don't have any saved grade books. Press RETURN "
              "to create a new grade book.\n")
        input("> ")
        file_path = new_file()
        EditXML.create_new_gradebook(file_path)
        EditXML.add_student(file_path)
        return file_path
    else:
        print("\nYou have {!s} grade books. Please select the XML file "
              "containing your class data from the list below:\n".format(
                total_books))
        print(gradebook_string)

    # Check to ensure that selected gradebook exists
    file_path = os.path.join(save_path, str(input("> ")) + '.xml')
    if os.path.exists(file_path):
        return file_path
    else:
        print("\nInvalid file name. Please choose another.")
        open_file()


def new_file():
    gradebook_name = str(input("What would you like to name this gradebook? "))
    file_path = os.path.join(save_path, gradebook_name + '.xml')
    return file_path


def main_menu():
    print("\nYou are using the file {!s}\n".format(file_name))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] View grades.")
    print("\t[2] Edit grades.")
    print("\t[3] File options for {!s}.".format(file_name))
    print("\t[4] Quit.")

    choice = str(input("> "))

    if choice == '1':
        view_menu()
    elif choice == '2':
        edit_menu()
    elif choice == '3':
        file_menu()
    elif choice == '4':
        quit()
    # Make XML files pretty for use during debugging
    elif choice == 'pretty':
        EditXML.make_pretty(file_name)
    else:
        print("Invalid selection.")
        main_menu()


def view_menu():
    end_prompt = "Press RETURN to continue.\n>"
    print("\nYou are using the file {!s}\n".format(file_name))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] View class report.")
    print("\t[2] View student report.")
    print("\t[3] View class statistics.")
    print("\t[4] Back to main menu.")

    choice = str(input("> "))

    if choice == '1':
        ParseXML.print_all_grades(file_name)
        input(end_prompt)
        view_menu()

    elif choice == '2':
        print("List of students:\n")
        ParseXML.list_students(file_name)
        print("\nEnter the name of a student, then press RETURN.")
        name = str(input("> \n"))

        if ErrorHandler.is_a_student(name, file_name):
            ParseXML.one_student_grades(file_name, name)
            input(end_prompt)
            view_menu()
        else:
            print("{!s} is not a student. Press RETURN to go back to"
                  " menu.".format(name))
            input("")
            view_menu()

    elif choice == '3':
        Statistics.get_statistics(file_name)
        input(end_prompt)
        view_menu()

    elif choice == '4':
        main_menu()
    else:
        print("Invalid selection.")
        view_menu()


def edit_menu():
    end_prompt = "Press RETURN to continue.\n>"
    print("\nYou are using the file {!s}\n".format(file_name))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] Add assignments")
    print("\t[2] Back to main menu.")

    choice = str(input("> "))

    if choice == '1':
        EditXML.add_assignment(file_name)
        input(end_prompt)
        main_menu()
    elif choice == '2':
        main_menu()


def file_menu():
    end_prompt = "Press RETURN to continue.\n>"
    print("\nYou are using the file {!s}\n".format(file_name))

    print("Choose an option by typing the number and pressing RETURN")
    print("\t[1] Export gradebook to text file.")
    print("\t[2] Open gradebook file.")
    print("\t[3] Create new gradebook")
    print("\t[4] Delete gradebook")
    print("\t[5] Back to main menu.")

    choice = str(input("> "))

    if choice == '1':
        ExportXML.export(file_name)
        input(end_prompt)
        main_menu()

    elif choice == '2':
        open_file()

    elif choice == '3':
        new_file()

    elif choice == '4':
        EditXML.delete_gradebook(file_name)
        open_file()

    elif choice == '5':
        main_menu()


if __name__ == '__main__':

    version_number = '0.5'

    # Save grade books to Documents, or create folder if it does not exist
    save_path = os.path.join(os.path.expanduser('~'), 'Documents',
                             'PyGB_Gradebooks')
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    print("\n\n\n")
    print("Welcome to PyGB version {!s}!".format(version_number))
    print("Created by Jason Handy.\n")
    print("To navigate the menus, type the prompts found in square brackets "
          "like these ---> []\n\n")
    print("Would you like to [open] an existing file, or create a [new] one?\n")
    file_choice = str(input("> "))

    if file_choice.lower() == 'o' or file_choice.lower() == 'open':
        file_name = open_file()
        main_menu()
    elif file_choice.lower() == 'n' or file_choice.lower() == 'new':
        file_name = new_file()
        EditXML.create_new_gradebook(file_name)
        EditXML.add_student(file_name)
        main_menu()
    else:
        print("\nInvalid command. Remember, you can only type prompts found in "
              "square brackets like these ---> []")
        print("\nTaking you to the file opening menu. Press RETURN to "
              "continue.\n")
        input("")
        file_name = open_file()
        main_menu()
