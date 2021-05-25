from deeppavlov import train_model
from deeppavlov.core.common.file import read_json
import json
import os


def train(config_path='model_config.json'):
    os.environ["CUDA_VISIBLE_DEVICES"] = "3"

    model_config = read_json(config_path)

    train_model(model_config)
    save(model_config, config_path)


def save(model_config, save_path):
    with open(save_path, 'w') as outfile:
        json.dump(model_config, outfile)


if __name__ == "__main__":
    train()
