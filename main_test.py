import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    heading = ['id', 'name', 'address']
    valueset = [[10, 'Kim', '123 Main'],
                [20, 'Bill', '345 Grand'],
                [30, 'Mary', '123 Blvd']
                ]
    students = main.makeDict(heading, valueset)
    print(f'Your return value is {students}')
    assert len(students) == 3
    assert students[0] == {'id': 10, 'name': 'Kim', 'address': '123 Main'}
    assert students[1] == {'id': 20, 'name': 'Bill', 'address': '345 Grand'}
    assert students[2] == {'id': 30, 'name': 'Mary', 'address': '123 Blvd'}

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())


def test_main_2():

    heading = ['A', 'B', 'C']
    valueset = [[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90],
                [100, 110, 120],
                ]
    students = main.makeDict(heading, valueset)
    print(f'Your return value is {students}')
    assert len(students) == 4
    assert isinstance(students[0], dict)
    assert students[0] == {'A': 10, 'B': 20, 'C': 30}
    assert students[1] == {'A': 40, 'B': 50, 'C': 60}
    assert students[2] == {'A': 70, 'B': 80, 'C': 90}
    assert students[3] == {'A': 100, 'B': 110, 'C': 120}
