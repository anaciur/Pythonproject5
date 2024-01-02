import os

directory_path3 = 'C:\\Users\\User\PycharmProjects\pythonProject5\\3rd_layer_Proteins_and_their_interactions'  # Replace with the actual path to your directory
directory_path4 = 'C:\\Users\\User\PycharmProjects\pythonProject5\\4th_layer_Proteins_and_their_interactions'  # Replace with the actual path to your directory


def delete(directory_path):
    try:
        # Get the list of files in the directory
        files = os.listdir(directory_path)

        # Iterate through each file and delete it
        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")

        print("All files in the directory have been deleted.")
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


delete(directory_path3)
delete(directory_path4)
