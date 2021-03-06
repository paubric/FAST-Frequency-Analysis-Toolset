from sample import Sample
from argparse import ArgumentParser

parser =ArgumentParser()
parser.add_argument("-f","--file_source", type=str)
parser.add_argument("-s","--string_source", type=str)
args = parser.parse_args()

if args.file_source is None and args.string_source is None:
    print("fast: error: no source specified")
    exit()
if args.file_source is not None and args.string_source is not None:
    print("fast: error: too many sources specified")
    exit()

sample = Sample()
if args.file_source is not None:
    sample.set_sample_from_file(args.file_source)
elif args.string_source is not None:
    sample.set_sample_from_string(args.string_source)

"""
# Print content of sample object
content = sample.data
print("Content:\t", content)
"""

# Print word count of sample object
word_count = sample.get_word_count()
print("Word count:\t\t", word_count)

# Print character count
char_count = sample.get_char_count()
print("Char count:\t\t", char_count)

# Print alphanumeric characters count
alphanum_count = sample.get_alphanum_count()
print("Alphanum count:\t\t", alphanum_count)

# Print average word length of sample object's data
avg_word_len = sample.get_avg_word_len()
print("Average word length:\t %.2f" % avg_word_len)

# Print percentage of alphanumeric characters
alphanum_percentage = sample.get_alphanum_percentage()
print("Alphanum percentage:\t", round(alphanum_percentage, 2), "%")

# Print blank line percentageo
blank_count = sample.get_char_appearances('\n\n')
lines_count = sample.get_char_appearances('\n')
blank_percentage = blank_count / lines_count * 100
print("Blank line percentage:\t", round(blank_percentage, 2), "%")

"""
# Print letter frequencies ordered alphabetically
dict = sample.get_letter_frequencies()
for item in sorted(dict):
    print(item," - ", round((dict[item]/alphanum_count)*100, 2), "%")

# Print letter frequencies ordered by popularity
dict = sample.get_letter_frequencies()
for item in sorted(dict.items(), key=lambda x: x[1], reverse=True):
    print(item[0]," - ", round(item[1]/alphanum_count*100, 2), "%")

# Print word frequencies ordered alphabetically
dict = sample.get_word_frequencies()
for item in sorted(dict, key=str.lower):
    print(item," - ", round((dict[item]/alphanum_count)*100, 2), "%")

# Print word frequencies ordered by popularity
dict = sample.get_word_frequencies()
for item in sorted(dict.items(), key=lambda x: x[1], reverse=True):
    print(item[0]," - ", round(item[1]/alphanum_count*100, 2), "%")
"""
