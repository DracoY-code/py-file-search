# Search a string in a directory
# ~ DracoY
import os


def search(path, string, file_type):
    """ Search a string at the path. """

    # Check path existence
    if not os.path.exists(path):
        path = '.'

    # Add slashes
    if not path.endswith('/') or path.endswith('\\'):
        path += '/'


    # List directory and iterate files
    for file in os.listdir(path):

        # Select files with file_type
        if file.endswith(file_type) or file.endswith('.' + file_type):

            # Surf file to check search exists
            f = open(path + file)
            
            line = f.readline()
            linenum = 1

            # Loop till EOL
            while line:
                # Search for string
                index = line.find(string)

                # Not found
                if (index != -1):
                    print(file, '[', linenum, ':', index, ']')

                # Read next line
                f.readline()

                linenum += 1

            # Close file
            f.close()


# __main__
path = input('Enter path: ')
string = input('Search: ')
file_type = input('File type: ')

search(path, string, file_type)

os.system('pause')