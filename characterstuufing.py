START = '$'
END = '$'
ESC = '*'

def stuffed_data(data):
    framed_data = [START]
    for byte in data:
        if byte == START or byte == END:
            framed_data.append(ESC)  # Add escape character before special chars
        framed_data.append(byte)
    framed_data.append(END)
    return framed_data

def unstuff_data(framed_data):
    if framed_data[0] != START or framed_data[-1] != END:
        raise ValueError("Invalid framed format")
    
    data = []
    i = 1
    while i < len(framed_data) - 1:
        byte = framed_data[i]
        if byte == ESC:
            i += 1  # Skip ESC and take next character
            if i < len(framed_data) - 1:
                data.append(framed_data[i])
        else:
            data.append(byte)
        i += 1
    return data

# Main Program
original_data = input("Enter data: ")
framed_data = stuffed_data(original_data)
print("Framed data:", ''.join(framed_data))
received_data = unstuff_data(framed_data)
print("Unstuffed data:", ''.join(received_data))
