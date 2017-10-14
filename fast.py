import sys
import string

def prep_file():
    file = open(sample)
    data = file.read()
    words = data.split()
    char_count = 0

    print("[*] Number of words in sample: "+str(len(words)))

    for word in words:
        char_count += len(word)

    print("[*] Number of characters in sample: "+str(char_count))
    return data, char_count

def prep_string():
    data = sample
    words = data.split()
    char_count = 0

    print("[*] Number of words in sample: "+str(len(words)))

    for word in words:
        char_count += len(word)

    print("[*] Number of characters in sample: "+str(char_count))
    return data, char_count

print("\nFAST - Frequency Analysis Toolset\n")

string_mode = False
file_mode = False

for item in sys.argv:
    if item == "-s":
        string_mode = True
    elif item == "-f":
        file_mode = True
    else:
        sample = item

if (len(sys.argv) == 1):
    print("[!] Error: No parameters specified")
    exit()
if (string_mode and file_mode):
    print("[!] Error: Both file mode and string mode specified")
    exit()
if (len(sys.argv) - int(string_mode) - int(file_mode) != 2):
    print("[!] Error: No sample specified")
    exit()

dict = {}

if (file_mode):
    data, char_count = prep_file()
    print("")
    for char in data:
        if char.isalnum():
            dict[char] = data.count(char)
    for char in sorted(dict):
        print(char+': '+str(dict[char])+' - '+str(round(dict[char]/char_count,2))+'%')
elif (string_mode):
    data, char_count = prep_string()
    print("")
    for char in data:
        if char.isalnum():
            dict[char] = data.count(char)
    for char in sorted(dict):
        print(char+': '+str(dict[char])+' - '+str(round(dict[char]/char_count,2))+'%')





