def find_highest_altitude(n, gains):
    current_altitude = 0
    highest_altitude = 0
    
    for gain in gains:
        current_altitude += gain
        if current_altitude > highest_altitude:
            highest_altitude = current_altitude
    
    return highest_altitude

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    gains = list(map(int, data[1:]))
    
    result = find_highest_altitude(n, gains)
    print(result)
