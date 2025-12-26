import cv2
import mediapipe as mp
import numpy as np
import torch
from scipy.spatial import distance as dist
from transformers import CLIPProcessor, CLIPModel