from reused import arguments, read_file

PATH="8thDay/input.txt"

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6

"""
Desc: Decode an image layer by layer, confiming proper image transfer
Param: path: filepath to the input data
"""
def part_1(path):
    global IMAGE_WIDTH, IMAGE_HEIGHT
    image = read_file(path or PATH,return_type=str,strip=True)[0]
    image_size = len(image)
    image_ptr = 0

    smallest_zeros = -1
    total = 0

    while image_ptr < image_size:
        layer = 0
        num_zeros = 0
        num_ones = 0
        num_twos = 0
        for idx in range(IMAGE_WIDTH):
            for jdx in range(IMAGE_HEIGHT):
                if image[image_ptr] == "0":
                    num_zeros += 1
                elif image[image_ptr] == "1":
                    num_ones += 1
                elif image[image_ptr] == "2":
                    num_twos += 1
                image_ptr += 1
        layer += 1

        if num_zeros < smallest_zeros or smallest_zeros == -1:
            smallest_zeros = num_zeros
            total = num_ones * num_twos

    print("The layer with the least 0s totalled %d (1's * 2's)" % (total))

"""
Desc: Analize the layers, and build a final coloured image from combination of layers
Param: path: filepath to the input data
"""
def part_2(path):
    global IMAGE_WIDTH, IMAGE_HEIGHT
    image = read_file(path or PATH,return_type=str,strip=True)[0]
    image_size = len(image)
    image_ptr = 0
    message = [["2" for i in range(IMAGE_WIDTH)] for j in range(IMAGE_HEIGHT)]

    while image_ptr < image_size:
        layer = 0
        for idx in range(IMAGE_HEIGHT):
            for jdx in range(IMAGE_WIDTH):
                if message[idx][jdx] == "2":
                    if image[image_ptr] != "2":
                        message[idx][jdx] = u"\u25A0" if image[image_ptr] == "1" else u"\u25A1"
                image_ptr += 1
        layer += 1

    print("The message that is produced is:")
    for idx in range(IMAGE_HEIGHT):
        for jdx in range(IMAGE_WIDTH):
            print(message[idx][jdx],end="")
        print()
    pass


if __name__ == '__main__':
    arguments(part_1,part_2)
    print()
