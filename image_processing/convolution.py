import numpy as np
import cv2
import os

# convert image to greyscale array
def processImage(image): 
  image = cv2.imread(image) 
  image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY) 
  return image

# Convolve the image from left to right
def convolveX(image, kernel, padding=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output

# Convolve image from top to bottom
def convolveY(image, kernel, padding=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through image
    for x in range(image.shape[0]):
        # Exit Convolution
        if x > image.shape[0] - xKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if x % strides == 0:
            for y in range(image.shape[1]):
                # Go to next row once kernel is out of bounds
                if y > image.shape[1] - yKernShape:
                    break
                try:
                    # Only Convolve if y has moved by the specified Strides
                    if y % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output






############## FEATURE EXTRACTION CONVOLUTIONS ################
def sobel_convolve(image_path, output_path, padding=0):
    image = processImage(image_path)
    kernelX = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])
    outputX = convolveY(image,kernelX,padding)
    kernelY = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
    output = convolveX(outputX, kernelY)
    cv2.imwrite(output_path, output)

def prewitt_convolve(image_path, output_path, padding=0):
    image = processImage(image_path)
    kernelX = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]])
    outputX = convolveY(image,kernelX,padding)
    kernelY = np.array([[-1, -1, -1],
                        [0, 0, 0],
                        [1, 1, 1]])
    output = convolveX(outputX, kernelY)
    cv2.imwrite(output_path, output)

def roberts_convolve(image_path, output_path, padding=0):
    image = processImage(image_path)
    kernelX = np.array([[1, 0],
                        [0, -1]])
    outputX = convolveY(image,kernelX,padding)
    kernelY = np.array([[0, 1],
                        [-1, 0]])
    output = convolveX(outputX, kernelY)
    cv2.imwrite(output_path, output)




############## FEATURE EXTRACTION CONVOLUTIONS ################

def guassian_convolve(image_path, output_path, padding=0):
    image = processImage(image_path)
    kernelX = np.array([[1/16, 2/16, 1/16],
                        [2/16, 4/16, 2/16],
                        [1/16, 2/16, 1/16]])
    output = convolveX(image, kernelX)
    cv2.imwrite(output_path, output)

def sharpening_convolve(image_path, output_path, padding=0):
    image = processImage(image_path)
    kernelX = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]])
    output = convolveX(image, kernelX)
    cv2.imwrite(output_path, output)

def embossing_convolve(image_path, output_path, padding=0):
    image = processImage(image_path)
    kernelX = np.array([[-2, -1, 0],
                        [-1, 1, 1],
                        [0, 1, 2]])
    output = convolveX(image, kernelX)
    cv2.imwrite(output_path, output)

def bold_sharpening_convolve(image_path, output_path, padding=0):
    image = processImage(image_path)
    kernelX = np.array([[-1, -1, -1],
                        [-1, 9, -1],
                        [-1, -1, -1]])
    output = convolveX(image, kernelX)
    cv2.imwrite(output_path, output)

def laplacian_convolve(image_path, output_path, padding=0):
    image = processImage(image_path)
    kernelX = np.array([[0, 1, 0],
                        [1, -4, 1],
                        [0, 1, 0]])
    output = convolveX(image, kernelX)
    cv2.imwrite(output_path, output)


def scharr_convolve(image_path, output_path, padding=0):
    scharr_kernel_real = np.array([[-3, 0, 3],
                                   [-10, 0, 10],
                                   [-3, 0, 3]])

    scharr_kernel_imaginary = np.array([[-3, -10, -3],
                                        [0, 0, 0],
                                        [3, 10, 3]])
    image = processImage(image_path)
    output_real = convolveX(image, scharr_kernel_real)
    output_imaginary = convolveX(image, scharr_kernel_imaginary)
    output = np.sqrt(output_real**2 + output_imaginary**2)
    cv2.imwrite(output_path, output)




if __name__ == '__main__':
    # Grayscale Image

    image_base = "/mnt/c/Users/paige/Desktop/old_microbe_images/Desmodesmus/"
    count = 0
    
    for image_name in os.listdir(image_base)[:10]:
        count += 1
        image_path = os.path.join(image_base, image_name)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/guassian_{count}.jpg"
        guassian_convolve(image_path, output_path, padding=2)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/sobel_{count}.jpg"
        sobel_convolve(image_path, output_path, padding=2)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/embossing_{count}.jpg"
        embossing_convolve(image_path, output_path, padding=2)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/sharpening_{count}.jpg"
        sharpening_convolve(image_path, output_path, padding=2)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/roberts_{count}.jpg"
        roberts_convolve(image_path, output_path, padding=2)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/prewitt_{count}.jpg"
        prewitt_convolve(image_path, output_path, padding=2)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/bold_{count}.jpg"
        bold_sharpening_convolve(image_path, output_path, padding=2)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/laplacian_{count}.jpg"
        laplacian_convolve(image_path, output_path, padding=2)
        output_path = f"/mnt/c/Users/paige/Desktop/convolutions/scharr_{count}.jpg"
        scharr_convolve(image_path, output_path, padding=2)
