import math

def main() -> None:
    length: str = input()
    numbers: list[str] = input().split()
    numbers: list[int] = [int(element) for element in numbers]
    result_lcm: int = math.lcm(*numbers)
    print(result_lcm)

if __name__ == "__main__":
    main()
