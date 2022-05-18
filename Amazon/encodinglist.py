tst_string = "abbcccdddd"


def encode_string(input: str) -> str:
    if not input:
        return ""
    char_counter = 0
    output_str = ""
    i = 0
    previous = input[0]
    while i < len(input):
        if input[i] == previous:
            char_counter += 1
        else:
            output_str += str(char_counter) + previous
            char_counter = 1
            previous = input[i]

        i += 1
    output_str += str(char_counter) + previous

    return output_str


print(encode_string(tst_string))
