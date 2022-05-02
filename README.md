# rotatepbm

A simple command line program for rotating PBM files.

## Description

Given a PBM file, the program will allow the image to be rotated 45, 90, or 180 degrees either clockwise or anti-clockwise. The result of the rotation will be written to a new output PBM file. The program contains validation and error handling to ensure that only PBM files can be used as input, and only files whose contents conform to the format's specification will be processed. The current functionality only supports ASCII (P1) PBM files, but could be extended to include PGM (P2) and PPM (P3) formats.

## Usage

Run the program (rotatepbm.py) in the command line. You will be prompted to enter a filename. If the given filename exists and has the .pbm extension, the program will prompt for the number of degrees to rotate the image by. Only 45, 90, and 180 are valid options. If 45 or 90 is entered, a final prompt will ask which direction to rotate the image: clockwise (c) or anti-clockwise (ac). Following this, the image will be rotated and the result written to a new PBM file.

17 test cases have been included as examples, located in the "tests" folder. They are listed below, along with whether they are expected to result in a successful rotation (valid) or not (invalid).

1: default example (valid)\
2: missing magic number (invalid)\
3: incorrect magic number (invalid)\
4: no comments (valid)\
5: multiple comments (valid)\
6: comments in random places (valid)\
7: only one dimension (invalid)\
8: three dimensions (invalid)\
9: no dimensions (invalid)\
10: dimensions do not match (invalid)\
11: image all on one line (valid)\
12: image with random spaces and returns (valid)\
13: very small image (valid)\
14: very wide image (valid)\
15: very tall image (valid)\
16: ints other than 0 and 1 (invalid)\
17: characters other than ints (invalid)