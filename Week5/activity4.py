def main():
    keys = ['a','b','c']
    values = [1,2,3]
    dictionary = {k:v for k, v in zip(keys, values)}
    dictionary["d"]= "4"
    print(dictionary)

if __name__ == "__main__":
    main()
