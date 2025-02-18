def unique_names(names1, names2):
    '''
    This function return a list removing repeated names
    '''
    names3 = names1 + names2
    names = set(names3)
    listname = [name for name in names]
    return listname


if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia