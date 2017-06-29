def outahere():
    import os
    print('Bye OS world.')
    os._exit(99)
    print('Never reached')


if __name__ == '__main__':
    outahere()
