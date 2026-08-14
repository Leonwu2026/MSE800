from ucimlrepo import fetch_ucirepo 

def main():
    print("Hello, World!")
    data = open("junk.txt")
    lines = data.readlines()
    number_of_lines = len(lines)
    print(f"1.Number of lines in the file: {number_of_lines}")


    with open("junk.txt", "w") as data:
        for line in lines:
            data.write(line.lower())
    data = open("junk.txt", "a")
    data.write("text file nanalyssis.\n")
    data.close()
    


if __name__ == "__main__":
    main()
    