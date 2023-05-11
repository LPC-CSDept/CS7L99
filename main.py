def main():
    IDs = [1001, 1002, 1003]
    Names = ['C Programming', 'Java Programming', 'Python Programming']

    for zobj in zip(IDs, Names):
        print(zobj)

    return zip(IDs, Names)


if __name__ == '__main__':
    main()
