import os


def scan_files(directory):
    file_list = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Add full file path (filename with extension)
            file_list.append(os.path.join(root, file))

    # If there are more than 15 files, print only the first 10
    if len(file_list) > 15:
        for i in range(10):
            print(file_list[i])
        print(f"[10 of {len(file_list)} files]")
    else:
        for file in file_list:
            print(file)


# Get the current directory
current_directory = os.getcwd()
print(f'Current directory: {current_directory}\n')

# Call the function
scan_files(current_directory)
