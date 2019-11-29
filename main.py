import errno
import os
import sys

import numpy as np
import cv2

from glob import glob

import textures


def vizDifference(diff):
    """This function normalizes the difference matrices so that they can be
    shown as images.
    """
    return (((diff - diff.min()) / (diff.max() - diff.min())) * 255).astype(np.uint8)


def runTexture(img_list, alpha):
    """This function administrates the extraction of a video texture from the
    given frames, and generates the three viewable difference matrices.
    """
    video_volume = textures.videoVolume(img_list)
    ssd_diff = textures.computeSimilarityMetric(video_volume)
    transition_diff = textures.transitionDifference(ssd_diff)
    idxs = textures.findBiggestLoop(transition_diff, alpha)
    print "Loop bounds: {}".format(idxs)

    # uncomment to generate markov based video
    # textures.gen_random_seq(img_list, 900, os.path.join("videos", "out", 'markov'), transition_diff, idxs[0], idxs[1])

    diff3 = np.zeros(transition_diff.shape, float)

    for i in range(transition_diff.shape[0]):
        for j in range(transition_diff.shape[1]):
            diff3[i, j] = alpha * (j - i) - transition_diff[j, i]

    return (vizDifference(ssd_diff),
            vizDifference(transition_diff),
            vizDifference(diff3),
            textures.synthesizeLoop(video_volume, idxs[0], idxs[1]))


def readImages(image_dir):
    """This function reads in input images from a image directory

    Note: This is implemented for you since its not really relevant to
    computational photography (+ time constraints).

    Args:
    ----------
        image_dir : str
            The image directory to get images from.

    Returns:
    ----------
        images : list
            List of images in image_dir. Each image in the list is of type
            numpy.ndarray.

    """
    extensions = ['bmp', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'jpeg',
                  'jpg', 'jpe', 'jp2', 'tiff', 'tif', 'png']

    search_paths = [os.path.join(image_dir, '*.' + ext) for ext in extensions]
    image_files = sorted(sum(map(glob, search_paths), []))
    images = [cv2.imread(f, cv2.IMREAD_UNCHANGED | cv2.IMREAD_COLOR) for f in image_files]

    bad_read = any([img is None for img in images])
    if bad_read:
        raise RuntimeError(
            "Reading one or more files in {} failed - aborting."
            .format(image_dir))

    return images


# The following section will run this file, save the three difference matrices
# as images, and complete the video frame extraction into the output folder.
# You will need to modify the alpha value in order to achieve good results.
if __name__ == "__main__":

    # Change alpha here or from the command line for testing
    try:
        alpha = float(sys.argv[1])
    except IndexError, ValueError:
        print("The required positional argument alpha was missing or " +
              "incompatible. You must specify a floating point value for " +
              "alpha.  Example usage:\n\n    python main.py 0.5\n")
        exit(1)

    video_dir = "candle"
    # video_dir = "fireplace"
    image_dir = os.path.join("videos", "source", video_dir)
    out_dir = os.path.join("videos", "out")

    try:
        _out_dir = os.path.join(out_dir, video_dir)
        not_empty = not all([os.path.isdir(x) for x in
                             glob(os.path.join(_out_dir, "*.*"))])
        if not_empty:
            raise RuntimeError("Output directory is not empty - aborting.")
        os.makedirs(_out_dir)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    print "Reading images."
    images = readImages(image_dir)

    print "Computing video texture with alpha = {}".format(alpha)
    diff1, diff2, diff3, out_list = runTexture(images, alpha)

    cv2.imwrite(os.path.join(out_dir, '{}_diff1.png'.format(video_dir)), diff1)
    cv2.imwrite(os.path.join(out_dir, '{}_diff2.png'.format(video_dir)), diff2)
    cv2.imwrite(os.path.join(out_dir, '{}_diff3.png'.format(video_dir)), diff3)

    for idx, image in enumerate(out_list):
        cv2.imwrite(os.path.join(out_dir, video_dir,
                    'frame{0:04d}.png'.format(idx)), image)
