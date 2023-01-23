def compress(data):
    compressed = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            compressed += str(count) + data[i-1]
            count = 1
    compressed += str(count) + data[-1]
    return compressed

def decompress(compressed):
    decompressed = ""
    num = ""
    for i in range(len(compressed)):
        if compressed[i].isnumeric():
            num += compressed[i]
        else:
            decompressed += compressed[i] * int(num)
            num = ""
    return decompressed

with open("input.txt", "r") as input_file:
    data = input_file.read()

compressed = compress(data)

with open("output.txt", "w") as output_file:
    output_file.write(compressed)

with open("output.txt", "r") as output_file:
    compressed = output_file.read()

decompressed = decompress(compressed)

with open("input.txt", "w") as input_file:
    input_file.write(decompressed)
