import os
import json
import glob
from modules import config

def format():
    json_dir = config.chats_folder
    output_file = config.dataset_file
    json_files = glob.glob(os.path.join(json_dir,