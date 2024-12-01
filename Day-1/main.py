def part_one(list_left, list_right):
    print("Part 1")
    total_distance: int = 0

    list_left.sort()
    list_right.sort()

    for i in range(len(list_left)):
        total_distance += (list_left[i] - list_right[i] if list_left[i] >= list_right[i] else list_right[i] - list_left[i])
    print(f"\tTotal Distance: {total_distance}")

def part_two(list_left, list_right):
    print("Part 2")
    similarity_score: int = 0

    for num_left in list_left:
        appearences = 0
        for num_right in list_right:
            if num_left == num_right:
                appearences += 1
        similarity_score += (num_left * appearences)
    print(f"\tSimilarity Score: {similarity_score}")

def main():
    list_left, list_right = [], []
    with open("./input.txt", "r") as f:
        for line in f:
            data = line.split()
            list_left.append(int(data[0]))
            list_right.append(int(data[-1]))

    part_one(list_left, list_right)
    part_two(list_left, list_right)

if __name__ == '__main__':
    main()