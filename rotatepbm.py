import os.path
import numpy as np
from scipy import ndimage

def main():
    filename, array = getArray()
    degrees = chooseDegrees()
    direction = chooseDirection(degrees)
    output = rotateImage(array, degrees, direction)
    writeFile(filename, output, degrees, direction)

def getArray():
    while True:
        filename = checkFile()
        array = readFile(filename)

        # If array does not match .pbm format, None will be returned; user will be prompted to enter a different filename
        if array is None:
            continue
        else:
            break

    return filename, array

def checkFile():
    while True:
        # Take filename from user input
        filename = input("Enter a PBM file: ")

        # Check that file exists; if not, prompt for filename again
        if not os.path.isfile(filename):
            print("Error: file does not exist")
            continue

        # Check that file is a .pbm file; if not, prompt for filename again
        if not filename.endswith(".pbm"):
            print("Error: must be a PBM file (.pbm)")
            continue
        else:
            break

    return filename

def readFile(filename):
    with open(filename) as f:
        # Read contents of the .pbm file to an array
        lines = f.readlines()

        # Filter comment lines from array
        lines = [line for line in lines if not line.startswith("#")]

        # Extract dimensions of the image from array
        dims = lines[1].split()

        # Check that magic number and dimensions of file conform to .pbm format
        if not lines[0].startswith("P1") or len(dims) != 2 or len(lines) < 3:
            print("Error: file contents do not conform to .pbm format")
            f.close()
            return

        # Specify width and height
        try:
            width, height = int(dims[0]), int(dims[1])
        except ValueError:
            # Catch error resulting from non-int characters present in dimensions
            print("Error: dimensions must be ints")
            return

        array = []

        # Create array from remainder of the .pbm file
        for line in lines[2:]:
            # Remove spaces from each line of the image
            line = line.strip().replace(" ", "")

            for i in line:
                # Convert each line to an array and append it to the array
                try:
                    i = [int(a) for a in str(i)]
                except ValueError:
                    # Catch error resulting from non-int characters present in array
                    print("Error: image contains non-int characters")
                    return
                array.append(i)

    f.close()

    # Check that array of image contains only 0s and 1s
    if not np.isin(array, [0, 1]).all():
        print("Error: contents of array do not conform to .pbm format")
        return
    array = reshapeArray(array, width, height)

    return array

def reshapeArray(array, width, height):
    try:
        # Reshape the array to match the given dimensions of the image
        array = np.reshape(array, (height, width))
    except ValueError:
        # Catch error resulting from dimensions not matching
        print("Error: given and actual dimensions do not match")
        return

    return array

def chooseDegrees():
    while True:
        try:
            # Take degrees to rotate from user input
            degrees = int(input("Choose 45, 90, or 180 degrees: "))
        except ValueError:
            # Check that a number has been entered; if not, prompt the user again
            print("Error: not a number")
            continue

        # Check that number is one of 45, 90, and 180 degrees; if not, prompt the user again
        if not degrees in {45, 90, 180}:
            print("Error: invalid degree entered")
            continue
        else:
            break

    return degrees

def chooseDirection(degrees):
    direction = "clockwise"

    # 180 degree rotation is the same regardless of direction; only ask for direction if 45 or 90 degrees
    if degrees in {45, 90}:
        while True:
            # Take direction to rotate from user input
            dirInput = str(input("Choose a direction to rotate: clockwise (c) or anti-clockwise (ac): "))

            # Check that direction is one of "c" and "ac"; if not, prompt the user again
            if not dirInput in {"c", "ac"}:
                print("Error: invalid direction entered")
                continue
            else:
                if dirInput == "ac":
                    direction = "anti-clockwise"
                break

    return direction

def rotateImage(array, degrees, direction):
    # Rotation is anti-clockwise by default; reverse degrees if clockwise was specified
    if direction == "clockwise":
        degrees = -abs(degrees)

    # Rotate the image by the specified degrees
    output = ndimage.rotate(array, degrees)
    return output

def writeFile(filename, output, degrees, direction):
    # Specify new filename for output
    outputFilename = filename.replace(".pbm", "_rotated.pbm")

    with open(outputFilename, "w", encoding="utf-8") as f:
        # Write magic number to output file
        f.write("P1\n")

        # Write comment containing information on the rotation performed to output file
        if degrees == 180:
            f.write("# " + filename + " rotated by " + str(degrees) + " degrees\n")
        else:
            f.write("# " + filename + " rotated by " + str(degrees) + " degrees " + direction + "\n")

        # Write width and height of the new array to output file
        f.write(str(len(output[0])) + " " + str(len(output)) + "\n")

        # Write the contents of the new array to output file
        np.savetxt(f, output, fmt="%1.0f")

    f.close()

if __name__ == "__main__":
    main()
