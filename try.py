try:
    lst = [0, 0, 0, 0]
    with open('data.txt', 'r') as f:
        count = 0
    for line in f.readlines():
        lst[count] = int(line)
    count += 1
    
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise