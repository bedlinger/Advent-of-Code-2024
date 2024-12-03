import re

def part_one(memory):
    print("Part 1")
    result: int = 0

    instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", memory)
    for instruction in instructions:
        nums = re.findall(r"[0-9]{1,3}", instruction)
        result += int(nums[0]) * int(nums[1])

    print(f"\tResult: {result}")

def part_two(memory):
    print("Part 2")
    result: int = 0
    is_enabled: bool = True

    instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", memory)
    for instruction in instructions:
        if instruction == "do()":
            is_enabled = True
        if instruction == "don't()":
            is_enabled = False
        if is_enabled and instruction != "do()" and instruction != "don't()":
            nums = re.findall(r"[0-9]{1,3}", instruction)
            result += int(nums[0]) * int(nums[1])

    print(f"\tResult: {result}")

def main():
    with open("./input.txt", "r") as f:
        data = f.read()
    part_one(data)
    part_two(data)

if __name__ == "__main__":
    main()