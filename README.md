# Video Textures

## Results

Following looped videos are the results of applying video textures techniques to two different videos. 

![Candle](videos/out/candle.gif)  
![Fireplace](videos/out/fireplace.gif)

## Synopsis

In this project I'm applying computational photography techniques to video, with the purpose of creating [video textures](http://www.cc.gatech.edu/cpl/projects/videotexture/) (infinitely looping pieces of video). These are basically gifs with very smooth transtitions. The process is also described in [Video Textures](http://cs.colby.edu/courses/F07/cs397/papers/schodl-videoTextures-sig00.pdf) (Scholdl, et al; SIGGRAPH 2000).


## Directions

### 1. Implement the functions in the `textures.py` file.

- `videoVolume`: Take a list containing image numpy arrays, and turn them into a single array which contains the entire video volume.
- `computeSimilarityMetric`: Find the "distance" between every pair of frames in the video.
- `transitionDifference`: Incorporate frame transition dynamics into a difference matrix created by computeSimilarityMetric.
- `findBiggestLoop`: Find an optimal loop for the video texture. (NOTE: part of your task is to determine the best value for the alpha parameter.)
- `synthesizeLoop`: Take our video volume and turn it back into a series of images, keeping only the frames in the loop you found. 


**Notes:**
- Images in the `videos/source/candle` directory are provided for testing. 

- Downsampling your images will save processing time during development. Larger images take longer to process.

- The `main.py` script reads files in the sorted order of their file name according to the conventions of python string sorting; it is essential that file names are chosen so that they are in sequential order or your results will be wrong. 

#### Finding a good alpha
The last bit of computation is the alpha parameter, which is a scaling factor. The size of the loop and the transition cost are likely to be in very different units, so we introduce a new parameter to make them comparable. We can manipulate alpha to control the tradeoff between loop size and smoothness. Large alphas prefer large loop sizes, and small alphas bias towards short loop sizes. You are looking for an alpha between these extremes (the goldilocks alpha). Your findBiggestLoop function has to compute this score for every choice of start and end, and return the start and end frame numbers that corresponds to the largest score. 

You must experiment with alpha to generate a loop of reasonable length (and that looks good) - more than one frame, and less than all of the frames. Alpha may vary significantly (by orders of magnitude) for different input videos.  When your coding is complete the main.py program will generate visualization images of the three difference matrices: similarity, transition, and scoring.  These matrices may help you identify good alpha values.


### 2. Use these function on your own input images to make a video texture

See the appendix, “Working with Video” for instructions to extract image frames from video clips, and tips on converting the image frames back to a gif. 


## Appendix - Working with Video

Working with video is not always user friendly. It is difficult to guarantee that a particular video codec will work across all systems. In order to avoid such issues, the inputs for this assignment are given as a sequence of numbered images.

You may use tools such as Gimp and others to break your own video into separate image frames. Alternatively, there are tools discussed below that you can use to split your own videos into frames, and to reassemble them into videos. These programs may not work for everyone depending on your operating system, software versions, etc. You will need to find something that works for you, so you can produce your results as a gif! Googling for image->gif tools online and asking other students on Piazza may help.

**ffmpeg (avconv)**
These are free and very widely used software for dealing with video and audio.

- ffmpeg is available [here](http://www.ffmpeg.org/)
- avconv is available [here](https://libav.org/avconv.html)

Example ffmpeg Usage:

You can use this command to split your video into frames:
```ffmpeg -i video.ext -r 1 -f image2 image_directory/%04d.png```

And this command to put them back together:
```ffmpeg -i image_directory/%04d.png out_video.gif```
