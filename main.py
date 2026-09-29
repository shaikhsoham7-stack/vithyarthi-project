from validator import validate_sequence
from analyzer import analyze_sequence
from sequence_operations import complement, reverse_sequence, reverse_complement


def display_analysis(sequence):
    result = analyze_sequence(sequence)

    print("\n--- Sequence Analysis ---")
    print("Sequence      :", sequence)
    print("Length        :", result["length"])
    print("A count       :", result["A"])
    print("T count       :", result["T"])
    print("G count       :", result["G"])
    print("C count       :", result["C"])
    print("GC content    :", f'{result["GC"]:.2f}%')
    print("AT content    :", f'{result["AT"]:.2f}%')


def main():
    sequence = ""

    while True:
        print("\n================================")
        print("       DNA SEQUENCE ANALYZER")
        print("================================")
        print("1. Enter DNA Sequence")
        print("2. Validate Sequence")
        print("3. Analyze Sequence")
        print("4. Find Complement")
        print("5. Find Reverse")
        print("6. Find Reverse Complement")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            sequence = input("Enter DNA sequence: ").strip().upper()

            if validate_sequence(sequence):
                print("Sequence saved successfully.")
            else:
                print("Invalid DNA sequence.")
                print("Only A, T, G and C are allowed.")
                sequence = ""

        elif choice == "2":
            if not sequence:
                print("Please enter a DNA sequence first.")
            elif validate_sequence(sequence):
                print("The sequence is valid.")
            else:
                print("The sequence is invalid.")

        elif choice == "3":
            if not sequence:
                print("Please enter a DNA sequence first.")
            else:
                display_analysis(sequence)

        elif choice == "4":
            if not sequence:
                print("Please enter a DNA sequence first.")
            else:
                print("Complement:", complement(sequence))

        elif choice == "5":
            if not sequence:
                print("Please enter a DNA sequence first.")
            else:
                print("Reverse:", reverse_sequence(sequence))

        elif choice == "6":
            if not sequence:
                print("Please enter a DNA sequence first.")
            else:
                print("Reverse Complement:", reverse_complement(sequence))

        elif choice == "7":
            print("Thank you for using DNA Sequence Analyzer.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
