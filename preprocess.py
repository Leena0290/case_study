import operator
import os

# Option 3: To pre-process the data before searching the index

def preprocess_search(input_str, file_directory):
    # Preprocess and create a search index
    final_check = {}
    final_result = {}
    input_str = input_str.lower()

    for filename in os.listdir(file_directory):
        # Define a dictionary that needs to be refreshed after every file is read
        op_dict = {}

        with open(file_directory + "/" + filename, "r", encoding="utf8") as curfile:
            for index, line in enumerate(curfile):
                line = line.lower()
                word_cnt = func_word_cnt(line.strip().split(" "),op_dict)

        # Pre-process the lines with word counts for all files
        final_check[filename] = word_cnt
    #return final_check

    #print(final_check.items())
    for keys,values in final_check.items():
        # Put 0 in the below get method since there is a chance that user enters a value which doesn't exist in file
        final_result[keys] = values.get(input_str,0)

    # Show the output as per the relevance criteria i.e sort the dictionary as per the highest value
    return dict(sorted(final_result.items(), key=operator.itemgetter(1),reverse=True))


def func_word_cnt(words,op_dict):
    for word in words:
        # if word contains any non-alphanumeric character then remove it and then proceed
        word = ''.join(c for c in word if c.isalnum())
        if word in op_dict:
            op_dict[word] = op_dict[word] + 1
        else:
            op_dict[word] = 1
    return op_dict


if __name__ == "__main__":
    print('Option 3: Preprocess & search via index')
    input_str = input("Enter a string: ")

    # Insert the directory in which source files are kept
    file_directory = "Source_Files"
    print(preprocess_search(input_str,file_directory))
