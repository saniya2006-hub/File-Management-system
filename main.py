
import os
import datetime

from modules.menu import show_menu

# Colour Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"


# Folder Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MYFILES = os.path.join(BASE_DIR, "MyFiles")
BACKUP = os.path.join(BASE_DIR, "Backup")

os.makedirs(MYFILES, exist_ok=True)
os.makedirs(BACKUP, exist_ok=True)


while True:

    show_menu()

    try:
        choice = int(input(YELLOW + "Enter your choice: " + RESET))

    except ValueError:
        print(RED + "Please enter a valid number!" + RESET)
        continue

    # 1. Create File
    if choice == 1:

        filename = input(CYAN + "Enter file name: " + RESET)

        try:
            filepath = os.path.join(MYFILES, filename)

            file = open(filepath, "x")
            file.close()

            print(GREEN + "File created successfully!" + RESET)

        except FileExistsError:
            print(YELLOW + "File already exists!" + RESET)

        except OSError:
            print(RED + "Unable to create file!" + RESET)

    # 2. Read File
    elif choice == 2:

        filename = input(CYAN + "Enter file name: " + RESET)

        try:
            filepath = os.path.join(MYFILES, filename)

            file = open(filepath, "r")
            content = file.read()

            print(PURPLE + "\nFile Content:" + RESET)
            print(WHITE + content + RESET)

            file.close()

        except FileNotFoundError:
            print(RED + "File does not exist!" + RESET)

        except OSError:
            print(RED + "Unable to read file!" + RESET)

    # 3. Write File
    elif choice == 3:

        filename = input(CYAN + "Enter file name: " + RESET)

        try:
            filepath = os.path.join(MYFILES, filename)

            file = open(filepath, "w")

            content = input(YELLOW + "Enter content: " + RESET)

            file.write(content)
            file.close()

            print(GREEN + "Content written successfully!" + RESET)

        except OSError:
            print(RED + "An error occurred!" + RESET)

    # 4. Append File
    elif choice == 4:

        filename = input(CYAN + "Enter file name: " + RESET)

        try:
            filepath = os.path.join(MYFILES, filename)

            file = open(filepath, "a")

            content = input(YELLOW + "Enter content to append: " + RESET)

            file.write("\n" + content)
            file.close()

            print(GREEN + "Content appended successfully!" + RESET)

        except OSError:
            print(RED + "An error occurred!" + RESET)

    # 5. Delete File
    elif choice == 5:

        filename = input(CYAN + "Enter file name to delete: " + RESET)

        try:
            filepath = os.path.join(MYFILES, filename)

            os.remove(filepath)

            print(GREEN + "File deleted successfully!" + RESET)

        except FileNotFoundError:
            print(RED + "File does not exist!" + RESET)

        except OSError:
            print(RED + "Unable to delete file!" + RESET)

    # 6. Rename File
    elif choice == 6:

        old_name = input(CYAN + "Enter current file name: " + RESET)
        new_name = input(CYAN + "Enter new file name: " + RESET)

        try:
            old_path = os.path.join(MYFILES, old_name)
            new_path = os.path.join(MYFILES, new_name)

            os.rename(old_path, new_path)

            print(GREEN + "File renamed successfully!" + RESET)

        except FileNotFoundError:
            print(RED + "File does not exist!" + RESET)

        except FileExistsError:
            print(YELLOW + "New file name already exists!" + RESET)

        except OSError:
            print(RED + "Unable to rename file!" + RESET)

    # 7. Search File
    elif choice == 7:

        filename = input(CYAN + "Enter file name to search: " + RESET)

        filepath = os.path.join(MYFILES, filename)

        if os.path.exists(filepath):
            print(GREEN + "File found successfully!" + RESET)

        else:
            print(RED + "File not found!" + RESET)

    # 8. Display Files
    elif choice == 8:

        try:
            files = os.listdir(MYFILES)

            if len(files) == 0:
                print(YELLOW + "Folder is empty!" + RESET)

            else:
                print(PURPLE + "\nFiles Available:" + RESET)

                for file in files:
                    print(CYAN + file + RESET)

        except OSError:
            print(RED + "Unable to access folder!" + RESET)

    # 9. Copy File
    elif choice == 9:

        filename = input(CYAN + "Enter file name to copy: " + RESET)
        new_filename = input(CYAN + "Enter new file name: " + RESET)

        source = os.path.join(MYFILES, filename)
        destination = os.path.join(MYFILES, new_filename)

        try:
            if os.path.exists(destination):
                print(YELLOW + "Destination file already exists!" + RESET)

            else:
                file1 = open(source, "r")
                content = file1.read()
                file1.close()

                file2 = open(destination, "x")
                file2.write(content)
                file2.close()

                print(GREEN + "File copied successfully!" + RESET)

        except FileNotFoundError:
            print(RED + "Source file does not exist!" + RESET)

        except OSError:
            print(RED + "Unable to copy file!" + RESET)

    # 10. File Information
    elif choice == 10:

        filename = input(CYAN + "Enter file name: " + RESET)

        filepath = os.path.join(MYFILES, filename)

        try:
            size = os.path.getsize(filepath)

            modified_time = os.path.getmtime(filepath)

            readable_time = datetime.datetime.fromtimestamp(modified_time)

            print(PURPLE + "\nFile Information:" + RESET)

            print(BLUE + "File Name: " + RESET + filename)
            print(BLUE + "File Size: " + RESET, size, "bytes")

            print(
                BLUE + "Last Modified: " + RESET,
                readable_time.strftime("%d-%m-%Y %I:%M:%S %p")
            )

        except FileNotFoundError:
            print(RED + "File does not exist!" + RESET)

        except OSError:
            print(RED + "Unable to get file information!" + RESET)

    # 11. Create Folder
    elif choice == 11:

        folder_name = input(CYAN + "Enter folder name: " + RESET)

        folder_path = os.path.join(MYFILES, folder_name)

        try:
            os.mkdir(folder_path)

            print(GREEN + "Folder created successfully!" + RESET)

        except FileExistsError:
            print(YELLOW + "Folder already exists!" + RESET)

        except OSError:
            print(RED + "Unable to create folder!" + RESET)

    # 12. Backup Files
    elif choice == 12:

        try:
            files = os.listdir(MYFILES)

            if len(files) == 0:
                print(YELLOW + "No files available for backup!" + RESET)

            else:
                for filename in files:

                    source_path = os.path.join(MYFILES, filename)
                    destination_path = os.path.join(BACKUP, filename)

                    if os.path.isfile(source_path):

                        if not os.path.exists(destination_path):

                            file1 = open(source_path, "r")
                            content = file1.read()
                            file1.close()

                            file2 = open(destination_path, "x")
                            file2.write(content)
                            file2.close()

                print(GREEN + "Backup completed successfully!" + RESET)

        except OSError:
            print(RED + "Unable to create backup!" + RESET)

    # 0. Exit
    elif choice == 0:

        print(GREEN + "\nThank you for using File Management System!" + RESET)
        break

    else:
        print(RED + "Invalid Choice!" + RESET)
