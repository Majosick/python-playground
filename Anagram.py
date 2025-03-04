def main():
    # Your main code goes here
    print("This is the Anagram program.")
    print("Enter 2 words and I'll tell whether they're anagrams")

    while True:
        first_word = input("Gimme first word")
        second_word = input("Gimme second word")
        first_array = sorted(list(first_word))
        second_array = sorted(list(second_word))
        if first_array == second_array:
            print("They're obviously anagrams")
        else:
            print("They're not anagrams")



if __name__ == "__main__":
    main()
