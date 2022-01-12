import pickle
import sys
import os

'''
    def retrieve_dict_obj(file_path):
        with open(file_path, "rb") as f:
            print()
            my_dict = dict()
            is_key = True
            for bytes_reader in f.readlines():
                if is_key is True:
                    key_value = bytes_reader.decode()[:-1]
                else:
                    field_value = bytes_reader.decode()[:-1]
                    my_dict.update({key_value: field_value})
                is_key = not is_key
            return my_dict

    def save_to_file(my_dict, output_file_path):
        with open(output_file_path, 'wb') as f:

            for k, v in my_dict.items():
                my_bytes_k = f'{str(k)}\n'.encode()
                my_bytes_v = f'{str(v)}\n'.encode()

                f.write(my_bytes_k)
                f.write(my_bytes_v)


    def main(arg='', my_dict = {}):
        output_file_path = sys.argv[1] if arg == '' else arg

        save_to_file(my_dict, output_file_path)
        print(retrieve_dict_obj(output_file_path))
        rf = remove_path(output_file_path)
        print("File removed" if rf else "File does not exist.")
        return rf

'''
# https://www.linkedin.com/learning/python-code-challenges/save-a-dictionary
def remove_path(output_file_path):
    try:
        os.remove(output_file_path)
    except:
        print("Exception has occurred")
        return False
    return True

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)
    
def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def main(arg='', my_dict = {}):
    output_file_path = sys.argv[1] if arg == '' else arg
    
    save_dict(my_dict, output_file_path)

    dict_from_file = load_dict(output_file_path)
    print(load_dict(output_file_path))

    rf = remove_path(output_file_path)
    print("File removed" if rf else "File does not exist.")

    return dict_from_file

if __name__ == '__main__': main()
