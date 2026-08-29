def main():
    Key1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'a']
    Value1 = [20, 3, 1, 88, 55, 92, 6, 90, 910]
    Key2 = ['u', 'b', 'o', 'x', 'e', 'a']
    Value2 = [200, 30, 10, 88, 55, 920]
    dic1 = {k: v for k, v in zip(Key1, Value1)}
    dic2 = {k: v for k, v in zip(Key2, Value2)}
    merged_dict = {**{k: v for k, v in dic1.items()if v % 2 != 0},
                   **{k: v for k, v in dic2.items()if v % 2 != 0}}

    print(merged_dict)

if __name__ == "__main__":
    main()
