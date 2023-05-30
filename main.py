def hasARE(words):
    """
    ########################################
    Code Your Program here
    ########################################
    """
    are = ['a', 'r', 'e']


def main():

    words = ['are', 'arrow', 'amore', 'aspire', 'assertive', 'arrogant', 'bartender', 'carter']
    are = ['a', 'r', 'e']
    ret = hasARE(words)
    print(f'The result is: {ret}')

    words = ['assertive', 'arrogant', 'bartender', 'carter', 'racer']
    are = ['a', 'r', 'e']
    ret = hasARE(words)
    print(f'The result is: {ret}')


if __name__ == '__main__':
    main()
