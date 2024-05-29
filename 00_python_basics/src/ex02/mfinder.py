import sys


def is_pattern(image):
    if len(image) != 3:
        return False
    for char in image:
        if len(char) != 5:
            return False
    m_pattern_positions = [
        (0, 0),
        (0, 4),
        (1, 0),
        (1, 1),
        (1, 3),
        (1, 4),
        (2, 0),
        (2, 2),
        (2, 4),
    ]
    for i in range(3):
        for j in range(5):
            if (i, j) in m_pattern_positions:
                if image[i][j] != "*":
                    return False
            else:
                if image[i][j] == "*":
                    return False
    return True


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    image = list(line.strip() for line in lines)
    print(is_pattern(image))
