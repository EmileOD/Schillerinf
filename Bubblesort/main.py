
Ints = []

def AbfrageVonInts():
    n = True
    while n:
        zahl = input("Geben Sie eine Zahl ein oder 'n', wenn Sie zur Sortierung wollen: ")
        if zahl != "n":
            try:
                zahlint = int(zahl)
                Ints.append(zahlint)  # Store the input number in the list
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")
        else:
            n = False  # Stop when 'n' is entered

def bubblesort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if the element found is greater
    return arr

AbfrageVonInts()

print("Unsortierte Liste:", Ints)


sorted_list = bubblesort(Ints)
print("Sortierte Liste:", sorted_list)
