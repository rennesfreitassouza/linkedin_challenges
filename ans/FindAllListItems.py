
# find all list items https://www.linkedin.com/learning/python-code-challenges/find-all-list-items
def index_all(lisToSearch, valueToSearchFor):
    indices = list()
    for index_higher_level_list in range(len(lisToSearch)):
        if lisToSearch[index_higher_level_list] == valueToSearchFor:
            indices.append( [ index_higher_level_list ] )
        elif isinstance(lisToSearch[ index_higher_level_list ], list):
            i_list = index_all(lisToSearch[ index_higher_level_list ], valueToSearchFor)
            for idx in i_list:
                index_para_valor_procurado_na_lista_de_entrada = [ index_higher_level_list ] + idx # list
                indices.append(index_para_valor_procurado_na_lista_de_entrada)
    return indices

def main():
    lisToSearch = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    valueToSearchFor = 2
    print(index_all(lisToSearch, valueToSearchFor))
    

if __name__ == '__main__': main()