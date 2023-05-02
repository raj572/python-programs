import heapq
from collections import defaultdict

def encode(s):
    # Step 1: Calculate frequency of each character in the input string
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1

    # Step 2: Construct Huffman tree using a priority queue
    heap = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Step 3: Generate the code table
    code_table = dict(heapq.heappop(heap)[1:])

    # Step 4: Generate the encoded string
    encoded_str = ''.join(code_table[c] for c in s)

    return encoded_str, code_table

def decode(encoded_str, code_table):
    # Invert the code table
    inv_code_table = {v: k for k, v in code_table.items()}

    # Decode the encoded string
    decoded_str = ''
    code = ''
    for bit in encoded_str:
        code += bit
        if code in inv_code_table:
            decoded_str += inv_code_table[code]
            code = ''

    return decoded_str

# Encode a string
s = 'hello world'
encoded_str, code_table = encode(s)
print('Encoded string:', encoded_str)
print('Code table:', code_table)

# Decode the encoded string
decoded_str = decode(encoded_str, code_table)
print('Decoded string:', decoded_str)
