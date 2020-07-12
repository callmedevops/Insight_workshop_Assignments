def toh(num, source, temporary, destination):
    if num == 1:
        print(f'Move disk 1 from {source} to {destination}')
        return

    toh(num - 1, source, destination, temporary)
    print(f'Move disk {num} from {source} to {destination}')
    toh(num - 1, temporary, source, destination)


number = int(input("Enter the number of disks: "))
toh(number, "Pole 1", "Pole 2", "Pole 3")
