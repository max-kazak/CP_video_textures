import cv2
import os

N_FRAMES = 200
SKIP = 100

def video_frame_generator(filename):
    """A generator function that returns a frame on each 'next()' call.

    Will return 'None' when there are no frames left.

    Args:
        filename (string): Filename.

    Returns:
        None.
    """
    video = cv2.VideoCapture(filename)

    # Do not edit this while loop
    while video.isOpened():
        ret, frame = video.read()

        if ret:
            yield frame
        else:
            break

    video.release()
    yield None


def main():
    vid_path = os.path.join('videos', 'fireplace.mp4')

    image_gen = video_frame_generator(vid_path)

    image = image_gen.next()
    i = 0
    skipped = 0
    while image is not None and i < N_FRAMES:
        if skipped < SKIP:
            skipped += 1
            continue
        out_path = os.path.join('videos', 'source', 'fireplace', '{:0>3d}.png'.format(i))

        image = cv2.resize(image, (0, 0), None, .5, .5)

        cv2.imwrite(out_path, image)

        image = image_gen.next()
        i += 1

        if i % 10 == 0:
            print i, ":", out_path


if __name__ == '__main__':
    main()
