import numpy as np
from scipy.signal import fftconvolve

def standard_convolution(image, kernel):
    """
    Apply standard convolution using fftconvolve.
    
    Args:
    - image: Input image (2D numpy array).
    - kernel: Convolution kernel (2D numpy array).
    
    Returns:
    - result: Convolved image.
    """
    result = fftconvolve(image, kernel, mode='same')
    return result

def depthwise_convolution(image, kernels):
    """
    Apply depthwise convolution using fftconvolve.
    
    Args:
    - image: Input image (3D numpy array with shape (height, width, channels)).
    - kernels: Depthwise convolution kernels (4D numpy array with shape (kernel_height, kernel_width, input_channels, output_channels)).
    
    Returns:
    - result: Convolved image.
    """
    result = np.zeros_like(image)
    for i in range(kernels.shape[-1]):
        result[..., i] = fftconvolve(image[..., i], kernels[..., i], mode='same')
    return result

def pointwise_convolution(image, kernel):
    """
    Apply pointwise (1x1) convolution using fftconvolve.
    
    Args:
    - image: Input image (3D numpy array with shape (height, width, channels)).
    - kernel: Pointwise convolution kernel (3D numpy array with shape (1, 1, input_channels, output_channels)).
    
    Returns:
    - result: Convolved image.
    """
    result = fftconvolve(image, kernel, mode='same')
    return result

def dilated_convolution(image, kernel, dilation_rate):
    """
    Apply dilated convolution using fftconvolve.
    
    Args:
    - image: Input image (2D numpy array).
    - kernel: Convolution kernel (2D numpy array).
    - dilation_rate: Dilation rate (integer).
    
    Returns:
    - result: Convolved image.
    """
    dilated_kernel = np.zeros((kernel.shape[0] + (kernel.shape[0] - 1) * (dilation_rate - 1),
                               kernel.shape[1] + (kernel.shape[1] - 1) * (dilation_rate - 1)))
    dilated_kernel[::dilation_rate, ::dilation_rate] = kernel
    result = fftconvolve(image, dilated_kernel, mode='same')
    return result

def transposed_convolution(image, kernel):
    """
    Apply transposed convolution using fftconvolve.
    
    Args:
    - image: Input image (2D numpy array).
    - kernel: Convolution kernel (2D numpy array).
    
    Returns:
    - result: Convolved image.
    """
    kernel = np.flipud(np.fliplr(kernel))
    result = fftconvolve(image, kernel, mode='full')
    return result
