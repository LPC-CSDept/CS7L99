def makeDict(heading, valueset):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    students = []

    for i in range(len(valueset)):
        students.append(dict(zip(heading, valueset[i])))
    return students


def main():
    heading = ['id', 'name', 'address']
    valueset = [[10, 'Kim', '123 Main'],
                [20, 'Bill', '345 Grand'],
                [30, 'Mary', '123 Blvd']
                ]

    students = makeDict(heading, valueset)
    #########################################
    for st in students:
        for k, v in st.items():
            print(f'{k} -> {v}\t', end=' ')
        print()
    #########################################
    # students
    # [{'id': 10, ‘name': 'Kim', 'Address': ‘123 Main’},
    # {'id': 20, 'nameI': 'Bill', ‘Address': '345 Grand'},
    # {'id': 30, 'name': 'Mary', 'Address': '123 Blvd'}]


if __name__ == '__main__':
    main()
