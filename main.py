'''
Author: fmsunyh fmsunyh@gmail.com
Date: 2023-09-30 21:13:42
LastEditors: fmsunyh fmsunyh@gmail.com
LastEditTime: 2023-09-30 23:05:28
FilePath: main.py
Description: desc
'''


import torch

from labml_nn.diffusion.stable_diffusion.scripts.text_to_image import sd_test

# from labml_nn.diffusion.stable_diffusion.model.autoencoder import Encoder


# encoder = Encoder(z_channels=4,
#                   in_channels=3,
#                   channels=128,
#                   channel_multipliers=[1, 2, 4, 4],
#                   n_resnet_blocks=2)


# model_scripted = torch.jit.script(encoder)
# model_scripted.save("./output/encoder.pt")

# torch.save(encoder.state_dict(), "./output/encoder.pth")

sd_test()



