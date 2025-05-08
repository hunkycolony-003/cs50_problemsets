def main():
    list = make_list()
    list = sort_list(list)
    removed_list = remove(list)
    print_list(removed_list, list)



def make_list():
    list = []
    i = 0
    while True:
        try :
            list.append(input().upper())
        except EOFError :
            return list



def sort_list(list):
    return sorted(list)


def remove(list):
    list_copy = list[:]
    i = 1
    while i < len(list_copy):
        if list_copy[i-1] == list_copy[i]:
            list_copy.pop(i)
        else :
            i += 1

    return list_copy



def print_list(removed_list, list):
        for i in removed_list:
            print (list.count(i), i)



main()
