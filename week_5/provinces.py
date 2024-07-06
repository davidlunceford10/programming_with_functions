with open("provinces.txt", "rt") as provinces_text:
    provinces_list = []
    for line in provinces_text:
        provinces_list.append(line.strip())
    print(provinces_list) 
    provinces_list.pop(0)
    provinces_list.pop()
    alberta_count = 0
    for line in provinces_list:
        if line == 'AB':
            index = provinces_list.index(line)
            provinces_list.pop(index)
            provinces_list.insert(index, 'Alberta')
            alberta_count += 1
    print(f'\nAlberta count: {alberta_count} times\n')    


