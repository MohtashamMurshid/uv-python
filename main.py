def main(nums):
    temparr = []
    duplicates_found = False
    
    for num in range(nums.__len__()):
        if num+1 < nums.__len__():
            if nums[num] == nums[num+1]:
                if not duplicates_found:
                    print("Duplicate found")
                    duplicates_found = True
            temparr.append(nums[num])
            print("new array", temparr)
            
    if not duplicates_found:
        print("No duplicates found")
    print("End of program")


if __name__ == "__main__":
    main(nums=[1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 10])
# This code is a simple Python script that defines a main function which takes a list of numbers as input.


