def main():
    # Your main code goes here
    print("This is the Anagram program.")
    print("Enter 2 words and I'll tell whether they're anagrams")

    while True:
        first_word = input("Gimme first word\n")
        second_word = input("Gimme second word\n")
        first_array = sorted(list(first_word))
        second_array = sorted(list(second_word))
        if first_array == second_array:
            print("They're obviously anagrams")
        else:
            print("They're not anagrams")
        decision = input("Do you want to continue? (Y/N)\n")
        if decision.lower() == "n":
            print("Bye then")
            break


if __name__ == "__main__":
    main()
