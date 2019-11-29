import cv2
import os


def circle_transition(filepath, coords, outpath):
    print 'processing ' + filepath
    img = cv2.imread(filepath, 0)

    print 'circle'
    cv2.circle(img, coords, 2, (0,255,0), 1)

    # cv2.imshow('img_after', img)
    # cv2.waitKey(0)
    print 'writing'
    cv2.imwrite(outpath, img)


def main():
    candle_coords = (91, 39)
    candle_path = os.path.join('videos', 'out', 'candle_diff3.png')
    candle_out = os.path.join('videos', 'out', 'candle_diff3_circled.png')
    circle_transition(candle_path, candle_coords, candle_out)

    fireplace_coords = (194, 19)
    fireplace_path = os.path.join('videos', 'out', 'fireplace_diff3.png')
    fireplace_out = os.path.join('videos', 'out', 'fireplace_diff3_circled.png')
    circle_transition(fireplace_path, fireplace_coords, fireplace_out)


if __name__ == '__main__':
    main()
