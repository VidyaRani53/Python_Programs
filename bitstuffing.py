def bit_stuffing(data):
    stuffed_data=[]
    consecutive_ones=0
    for bit in data:
        stuffed_data.append(bit)
        if bit==1:
            consecutive_ones+=1
        else:
            consecuyive_ones=0
        if consecutive_ones==5:
            stuffed_data.append(0)
            consecutive_ones=0
    return stuffed_data
def read_bits():
    user_input=input("enter a sequence of bits(0's and 1's)")
    data=[]
    for char in user_input:
        if char=='1' or char=='0':
            data.append(int(char))
        else:
            print("invalid input:only 0's and 1's are allowed")
            return []
    return data
if __name__=="__main__":
    original_data=read_bits()
    if not original_data:
        exit()
stuffed_data=bit_stuffing(original_data)
print("stuffed_data:",stuffed_data)
print("original_data:",original_data)
