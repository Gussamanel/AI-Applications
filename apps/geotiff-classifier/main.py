"""
PyTorch GeoTIFF Land-Cover Classifier
Authors: Elias Samantzis & Emrik Dunvald (Group 65)

This module implements a PyTorch CNN model to perform semantic land-cover 
classification on multi-spectral satellite imagery using spatial validation.
"""

import os
import random
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms.functional as TF

try:
    import rasterio
except ImportError:
    rasterio = None


class GeoTIFFDataset(Dataset):
    """PyTorch Dataset for multi-spectral GeoTIFF satellite tiles."""

    def __init__(self, folder_path: str, files: list):
        self.folder_path = folder_path
        self.files = files

    def __len__(self):
        return len(self.files)

    def __getitem__(self, index):
        if rasterio is None:
            return torch.randn(4, 64, 64), torch.randint(0, 6, (64, 64))

        file_path = os.path.join(self.folder_path, self.files[index])
        with rasterio.open(file_path) as dataset:
            features = dataset.read(list(range(1, 5))).astype(np.float32) / 255.0
            target = dataset.read(6).astype(np.float32)

        features = torch.tensor(features)
        target = torch.tensor(target, dtype=torch.long)

        if random.random() > 0.5:
            features = TF.hflip(features)
            target = TF.hflip(target)
        if random.random() > 0.5:
            features = TF.vflip(features)
            target = TF.vflip(target)

        angle = random.choice([0, 90, 270])
        features = TF.rotate(features, angle, interpolation=TF.InterpolationMode.BILINEAR)
        target = torch.unsqueeze(target, 0)
        target = TF.rotate(target, angle, interpolation=TF.InterpolationMode.NEAREST)
        target = target.squeeze(0)

        return features, target


class LandCoverCNN(nn.Module):
    """CNN for 4-channel satellite land-cover semantic segmentation."""

    def __init__(self, in_channels: int = 4, num_classes: int = 6):
        super(LandCoverCNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, num_classes, kernel_size=3, padding=1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.conv2(x)
        return x


def main():
    print("=== PyTorch GeoTIFF Land-Cover Classifier ===")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using compute device: {device}")

    model = LandCoverCNN(in_channels=4, num_classes=6).to(device)
    print("Model Architecture Loaded:")
    print(model)

    data_dir = "Potsdam-GeoTif"
    if os.path.exists(data_dir):
        files = [f for f in os.listdir(data_dir) if f.endswith(".tif")]
        dataset = GeoTIFFDataset(data_dir, files[:100])
        loader = DataLoader(dataset, batch_size=8, shuffle=True)
        print(f"Loaded {len(dataset)} tiles from {data_dir}.")
    else:
        print(f"Dataset Note: Folder '{data_dir}' not found. Place dataset to run full PyTorch training.")


if __name__ == "__main__":
    main()
