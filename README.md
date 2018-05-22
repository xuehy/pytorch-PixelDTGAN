# Pixel Level Domain Transfer
A pytorch remake of the implementation of "Pixel-Level Domain Transfer" [PixelDTGAN](https://github.com/fxia22/PixelDTGAN).

# Dependency
- ```pytorch >= 0.4.0```
- [visdom](https://github.com/facebookresearch/visdom).
- [opencv](https://github.com/opencv/opencv)

# Training

To train the model, put the LOOKBOOK dataset under repository, resize images to 64*64. Prepare the dataset using `tool/prepare_data.py`.
Then goto src dir and run
```
python3 train.py
```

# Monitor the performance


- Install [visdom](https://github.com/facebookresearch/visdom).
- Start the visdom server with ```python3 -m visdom.server -port 5274```
- Open this URL in your browser: `http://localhost:5274

