## Executive Summary

This project aims to automate the diameter measurement for CNT TEM images.
As of September 8, 2020, it can distinguish regions of interest that contain
a CNT suitable for measurement from regions of interest that do not. This is
the first block toward automate the full process.

### Problem Statement

Researchers are interested in measuring the distribution of diameters in the samples they grow. Currently, diameter measurements are taken manually.
One method for performing measurement manually is to use a MATLAB script to draw a line across a CNT.
The script automatically records the length of that line and produces a labelled image.
Each dataset, consisting of around 30 images, takes about 2 hours to process.
Datasets are processed year-round at a rate of about 1 per week. Thus, automating the process could save on the order of 100 hours of labor per year.


### Conclusions

Data was organized and used to train and CNN classifier to recognize good CNT measurement locations. Validation accuracy just below 90% was achieved.

The code developed is extensible to Step 2,  measuring diameters.


### Future Work

* Finding good CNT measurement locations within an image comes next.
* More datasets may increase validation accuracy.
* Explore generating segmentation labels


### Data Analysis

Data is note stored in github. This data was generously provided by Steven Buchsbaum at Lawrence Livermore National Laboratory and I have not asked for permission to share is publicly, yet. Contact me at maxwiedmann@gmail.com if you are interested in the data.

This program currently uses to jupyter notebooks: `build_df.ipynb` to assemble a dataframe containing regions of interest and `training_classifying.ipynb` to train a CNN to distinguish images that contain measureable CNTs from images that do not. `build_df.ipynb` will export the generated dataframe to a pickle object, which can be read in by `training_classifying.ipynb`.

The generated pandas dataframe has the following features:

|Feature|Type|Description|
|------|------|------|------|
|index|index|self explanatory|
|name|string|The name of each entry. Naming convention good CNT images is dataset_rawfilename-measurement-augmentation. For example 193_'0.jpg-6-0 means sampleset 193, raw file 0.jpg, measurement 6 within that file, augmentation 0 (no flips or rotations). For negative images '_neg' comes directly after the file name and is then followed by a number, indicating the order it was created. Negative images are not augmented.|
|img|numpy array|An n x n numpy array containing an image of a region of interest that could or could not contain a measured CNT.|
|diameter|int|The measured diameter of the CNT, in pixels. Needs to be converted to nm manually. Equals 0 for negative images.|
|has_cnt|boolean|Indicates if the image contains a good CNT or not.|
|no_cnt|boolean|The negative of `has_cnt` to make keras happy with classification.|



### Classes and Functions

class: `cnt_mat_fig`

This class has a constructor for reading in CNT .fig files. It has built in methods for creating a list of good CNT images of a specified size, .get_ROIS, and a list of negative images of a specified size, get_negs. Always choose the same sizes for both!

function `flip_rot`:

Takes a list of images, imgs, and returns a list of images imgs_out,
where each image is a rotation, flip, or both of an image in imgs.

function: `add_cnt_data`

Used to fill at dataframe with a `cnt_mat_fig` class object.

function: `read_dir`

This function is used to run `add_cnt_data` on all files in a provided directory.

Plots generated are located in the [images](./images/) directory.
