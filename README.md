
## Enhancing gpt-3.5-turbo's Role-play Capability

This project is a detailed guide on how to fine-tune OpenAI's gpt-3.5-turbo to work better in role-play scenarios.
Some of the key limitations and considerations are:
- Currently, you can only fine-tune `gpt-3.5-turbo` (`gpt-3.5-turbo-0613` specifically). Future fine-tuning for GPT-4 is planned but might involve additional costs.
- The cost of fine-tuning is low, but the inference cost for the fine-tuned model may be significantly higher.
- The fine-tune model cannot be shared between OpenAI accounts.
- Training data is passed through OpenAI's Moderation API to ensure it meets the company's safety standards. This means all training data must be strictly SFW.
- The owner of an account is notified via email when the fine-tuning process is completed.

The process of fine-tuning is explained in detail, starting from the pre-requisites needed to prepare your dataset all the way to how you can check your model's status during the training process. Some preliminary knowledge and setup, such as having Python installed and having a valid OpenAI key, are essential before proceeding.

Along with the steps needed to prepare your dataset for training, it also outlines how to polish and prepare your chat files, as well as some tips on how to ensure better results from your training. The repository also includes basic checks to ensure your dataset is valid and how to initiate the fine-tuning process with OpenAI.

Finally, it provides resources and links that give further in-depth information on OpenAI's fine-tuning. Please note that the provided code is licensed under WTFPL. Some parts of `data_check.py` were taken from OpenAI's fine-tuning guide.