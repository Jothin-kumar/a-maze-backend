encodeChrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!._$,()"
decodeToNum = lambda a: encodeChrs.index(a) + 1
decodeToCoords = lambda alpha: (decodeToNum(alpha[0]), decodeToNum(alpha[1]))

lvl_size = {
    "easy": 25,
    "medium": 49,
    "hard": 69,
}

def validate_maze(data: str, level: str):

    if len(data) < 6:
        raise ValueError("Too short")
    if [c for c in data if c not in encodeChrs[:lvl_size[level]]] != ["-", "-"]:
        raise ValueError("Invalid character(s) found")

    path = [
        decodeToCoords(data[2:4]),  # End
        decodeToCoords(data[0:2]),  # Start
    ]

    data = data[4:].split("-")
    if not all([len(d) % 2 == 0 for d in data]):
        raise ValueError("Invalid coordinates")

    d = data[0]
    for i in range(0, len(d), 2):
        path.insert(1, decodeToCoords(d[i:i+2]))
    for i in range(len(path)-1):
        if abs(path[i][0] - path[i+1][0]) + abs(path[i][1] - path[i+1][1]) != 1:
            raise ValueError("Lack of continuity in correct path")

    if len(set(path)) != len(path):  # Check for duplicates
        raise ValueError("Repetition found in correct path")

    # Now, the maze data is valid
    return

def handler(context, basicio):
    data = basicio.get_argument('maze-data')
    lvl = basicio.get_argument('level') or "medium"
    print = basicio.write
    set_status = basicio.set_status
    try:
        validate_maze(data, lvl)
        print("Valid maze data")
        set_status(200)
    except ValueError as e:
        print(str(e))
        set_status(400)

    context.log('Successfully executed basicio function')
    context.close()
