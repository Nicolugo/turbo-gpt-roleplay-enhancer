
import os
import argparse
import datetime

from colorama import just_fix_windows_console, Fore, Back, Style
just_fix_windows_console()

import openai


from modules import format_dataset, data_check, config

def upload_file():
    file = openai.File.create(
        file=open(config.dataset_file, "rb"),
        purpose='fine-tune'
    )
    with open("file_id.txt", "w") as f:
        f.write(file["id"])

def start_finetune():
    job = openai.FineTuningJob.create(