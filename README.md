# Video Textures

**Important Note:** This assignment is subject to the "Above & Beyond" rule. In summary: meeting all stated requirements will earn 90%; the last 10% is reserved for individual effort to research, implement, and report some additional high-quality work on this topic beyond the minimum requirements. Your A&B work must be accompanied by discussion of the computational photographic concepts involved, and will be graded based on the level of effort, and quality of your results and documentation in the report. (Please review the full explanation of this rule in the syllabus or on Piazza.)


## Synopsis

In this assignment we will be applying our computational photography magic to video, with the purpose of creating [video textures](http://www.cc.gatech.edu/cpl/projects/videotexture/) (infinitely looping pieces of video). These are basically gifs with very smooth transtitions, as seen in Lecture 06-02, Video Textures. The process is also described in [Video Textures](http://cs.colby.edu/courses/F07/cs397/papers/schodl-videoTextures-sig00.pdf) (Scholdl, et al; SIGGRAPH 2000).


## Instructions

### 1. Implement the functions in the `textures.py` file.

- `videoVolume`: Take a list containing image numpy arrays, and turn them into a single array which contains the entire video volume.
- `computeSimilarityMetric`: Find the "distance" between every pair of frames in the video.
- `transitionDifference`: Incorporate frame transition dynamics into a difference matrix created by computeSimilarityMetric.
- `findBiggestLoop`: Find an optimal loop for the video texture. (NOTE: part of your task is to determine the best value for the alpha parameter.)
- `synthesizeLoop`: Take our video volume and turn it back into a series of images, keeping only the frames in the loop you found. 

The docstrings of each function contain detailed instructions. You are **strongly** encouraged to write your own unit tests based on the requirements. The `test_textures.py` file is provided to get you started. Your code will be evaluated on input and output type (e.g., uint8, float, etc.), array shape, and values. (Be careful regarding arithmetic overflow!) When you are ready to submit your code, you can send it to the autograder for scoring by running `omscs submit code` from the root directory of the project folder. Remember that you will only be allowed to submit three times every two (2) hours. In other words, do *not* try to use the autograder as your test suite.

**Notes:**
- Images in the `videos/source/candle` directory are provided for testing -- _do not include these images in your submission_ (although the output should appear in your report).

- Downsampling your images will save processing time during development. Larger images take longer to process, and may cause problems for the VM and autograder which are resource-limited.

- The `main.py` script reads files in the sorted order of their file name according to the conventions of python string sorting; it is essential that file names are chosen so that they are in sequential order or your results will be wrong. 

#### Finding a good alpha
The last bit of computation is the alpha parameter, which is a scaling factor. The size of the loop and the transition cost are likely to be in very different units, so we introduce a new parameter to make them comparable. We can manipulate alpha to control the tradeoff between loop size and smoothness. Large alphas prefer large loop sizes, and small alphas bias towards short loop sizes. You are looking for an alpha between these extremes (the goldilocks alpha). Your findBiggestLoop function has to compute this score for every choice of start and end, and return the start and end frame numbers that corresponds to the largest score. 

You must experiment with alpha to generate a loop of reasonable length (and that looks good) - more than one frame, and less than all of the frames. Alpha may vary significantly (by orders of magnitude) for different input videos.  When your coding is complete the main.py program will generate visualization images of the three difference matrices: similarity, transition, and scoring.  These matrices may help you identify good alpha values.


### 2. Use these function on your own input images to make a video texture - _READ CAREFULLY_

See the appendix, “Working with Video” for instructions to extract image frames from video clips, and tips on converting the image frames back to a gif. Host your gif & input frames on Google Drive, Dropbox, or similar. Get the correct sharing link in your report so that anyone with the link may view the gif. Once you’re finished with this, give yourself a pat on the back (or a hug!) because you’re done with the homework assignments!

**REMINDER:** You are responsible to ensure that links to your GIFs in your report function properly. _We will not accept regrade requests if your images are missing because the links are expired or unviewable._

### 3. Above & Beyond

- Using your own video instead of (or in addition to) using clips from the web will count towards above and beyond credit for this assignment.

Keep in mind:
- Earning the full 10% for A&B is typically _very_ rare; you should not expect to reach it unless your results are _very_ impressive.
- Attempting something very technically difficult does not ensure more credit; make sure you document your effort even if it doesn't pan out.
- Attempting something very easy in a very complicated way does not ensure more credit.


### 4. Complete the report

Make a copy of the [report template](https://docs.google.com/presentation/d/1_TZhqg9QDCrc2ocwJyHdN2W-3wpnTY9NlidzTcOzd5w/edit?usp=sharing) and answer all of the questions. Save your report as `report.pdf` in the project directory.


### 5. Submit the Code

**Note:** Make sure that you have completed all the steps in the [instructions](../README.md#virtual-machine-setup) for installing the VM & other course tools first.

Follow the [Project Submission Instructions](../README.md#submitting-projects) to upload your code to [Bonnie](https://bonnie.udacity.com) using the `omscs` CLI:

```
$ omscs submit code
```


### 6. Submit the Report

Save your report as `report.pdf`. Your final artifact & images should be uploaded to a private folder shared with instructors through a link in your report (e.g., dropbox, google drive, etc.). DO NOT UPLOAD YOUR RESOURCES WITH YOUR REPORT. Zip your report into a single zip archive and submit the file via Canvas. You may choose any name you want for the zip archive, e.g., `assignment7.zip`. Canvas will automatically rename the file if you resubmit, and it will have a different name when the TAs download it for grading. (In other words, you only need to follow the required naming convention for `report.pdf` inside your submission archive; don't worry about the name for the single zip archive.) YOUR REPORT SUBMISSION FOR THIS PROJECT DOES NOT NEED TO INCLUDE THE CODE, WHICH MUST BE SEPARATELY SUBMITTED TO BONNIE FOR SCORING.

**Note:** The total size of your project must be less than 8MB for this project. If your submission is too large, you can reduce the scale of your report. You can compress your report using [Smallpdf](https://smallpdf.com/compress-pdf).


## Criteria for Evaluation

Your submission will be graded based on:

  - Correctness of required code
  - Creativity & overall quality of results
  - Completeness and quality of report


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
