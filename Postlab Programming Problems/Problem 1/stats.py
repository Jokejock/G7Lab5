import mode  # Import mode.py
import median  # Import median.py
import mean  # Import mean.py

def main():
    file_name = input("Enter file name: ")

    try:
        #Read the content of the file
        with open(file_name, 'r') as file:
            content = [line.strip() for line in file]

            #Attempt to determine if the program contains words or numbers
            try:
                #Converts the content to numbers
                numbers = [float(item) for item in content]
                # Call median.py, mean.py, and mode.py to calculate their respective statistics
                print("Numbers from file:", numbers)
                median.main(numbers)  # This will call the median function from median.py
                mean.main(numbers)    # This will call the mean function from mean.py
                print("Mode:", mode.mode(numbers))  # Calling mode from mode.py

            except ValueError:
                # If conversion fails, assume it's a list of words
                words = [item.upper() for item in content]  # Convert words to uppercase for case-insensitivity
                print("Words from file:", words)
                print("Mode (most frequent word):", mode.mode(words))  # Mode for words (strings)

    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")

if __name__ == "__main__":
    main()