import main
import io
import sys
import re
import math


def test_main_1():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = 'are arrow amore aspire aero'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    assert len(main.main.result) == 3
    assert main.main.result[0] == 'are'
    assert main.main.result[1] == 'amore'
    assert main.main.result[2] == 'aspire'


def test_main_2():
    captureout = io.StringIO()
    sys.stdout = captureout
    datastr = 'assertive arrogant bartender carter racer'
    sys.stdin = io.StringIO(datastr)

    main.main()
    sys.stdout = sys.__stdout__
    print('captured ', captureout.getvalue())
    lines = captureout.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\w]*1'
    # regex_string += r'[\w,\w]*3'
    # regex_string += r'[\w,\w]*5'
    # regex_string += r'[\w,\w]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != none
    # print(res.group())
    assert len(main.main.result) == 3
    assert main.main.result[0] == 'assertive'
    assert main.main.result[1] == 'bartender'
    assert main.main.result[2] == 'carter'
