ordered = input("Is the collection ordered? Enter T or F.")
if ordered == "F":
    print("The collection is a set.")
    print("It is unordered and unchangeable with no duplicates.")

else:
    changeable = input("Is the collection changeable? Enter T or F.")
    if changeable == "F":
        print("The collection is a tuple.")
        print("It is ordered and unchangeable with no duplicates.")

    else:
        duplicates = input("Does the collection allow duplicates? Enter T or F.")
        if ordered == "T" and changeable == "T" and duplicates == "F":
            print("The collection is a dictionary.")
            print("It is ordered and changeable with no duplicates.")
        elif ordered == "T" and changeable == "T" and duplicates == "T":
            print("The collection is a list.")
            print("It is ordered and changeable with duplicates.")
        else:
            print("The collection is not defined.")
