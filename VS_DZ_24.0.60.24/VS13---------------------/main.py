# завдання 1
# def compare_files(file1, file2):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()
        
#         if lines1!= lines2:
#             for line1, line2 in zip(lines1, lines2):
#                 if line1!= line2:
#                     print(f"File 1: {line1.strip()}")
#                     print(f"File 2: {line2.strip()}")
#                     break
#             else:
#                 print("Files are identical")

# compare_files('file1.txt', 'file2.txt')
#---------------------------------------------------------------
# завдання 2
# def create_stats_file(input_file, output_file):
#     with open(input_file, 'r') as f:
#         text = f.read()
        
#         char_count = len(text)
#         line_count = len(text.splitlines())
#         vowel_count = sum(1 for char in text if char.lower() in 'aeiouy')
#         consonant_count = sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiouy')
#         digit_count = sum(1 for char in text if char.isdigit())
        
#         with open(output_file, 'w') as f_out:
#             f_out.write(f"Character count: {char_count}\n")
#             f_out.write(f"Line count: {line_count}\n")
#             f_out.write(f"Vowel count: {vowel_count}\n")
#             f_out.write(f"Consonant count: {consonant_count}\n")
#             f_out.write(f"Digit count: {digit_count}\n")
# create_stats_file('input.txt', 'tats.txt')
#---------------------------------------------------------------
# завдання 3
# def remove_last_line(input_file, output_file):
#     with open(input_file, 'r') as f:
#         lines = f.readlines()
        
#         with open(output_file, 'w') as f_out:
#             f_out.writelines(lines[:-1])
# remove_last_line('input.txt', 'output.txt')
#---------------------------------------------------------------
# завдання 4
# def find_longest_line(file):
#     with open(file, 'r') as f:
#         lines = f.readlines()
        
#         longest_line = max(lines, key=len)
#         print(f"Longest line length: {len(longest_line.strip())}")
# find_longest_line('input.txt')
#---------------------------------------------------------------
# завдання 5
# def count_word(file, word):
#     with open(file, 'r') as f:
#         text = f.read()
        
#         word_count = text.lower().count(word.lower())
# count_word('input.txt', 'example')
#---------------------------------------------------------------
# завдання 6
# def find_and_replace(file, old_word, new_word):
#     with open(file, 'r') as f:
#         text = f.read()
        
#         new_text = text.replace(old_word, new_word)
        
#         with open(file, 'w') as f:
#             f.write(new_text)
# find_and_replace('input.txt', 'old', 'new')