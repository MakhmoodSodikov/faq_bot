import json
import os

from deeppavlov.core.common.file import read_json
from deeppavlov import configs, train_model


def train():
    pred_config_path = 'pred_model_config.json'
    intent_config_path = 'intent_model_config.json'

    os.environ["CUDA_VISIBLE_DEVICES"] = "3"

    pred_model_config = read_json(pred_config_path)

    train_model(pred_model_config)
    save(pred_model_config, pred_config_path)

    train_data = read_json("/home/sodikov_mmo/faq_bot/downloads/intent_catcher_data/train.json")
    test_data = read_json("/home/sodikov_mmo/faq_bot/downloads/intent_catcher_data/test.json")
    valid_data = read_json("/home/sodikov_mmo/faq_bot/downloads/intent_catcher_data/valid.json")

    intent_model_config = read_json(configs['intent_catcher']['intent_catcher'])
    intent_model_config['metadata']['variables']['ROOT_PATH'] = '/home/sodikov_mmo/faq_bot'
    intent_model_config['chainer']['pipe'][1]['number_of_intents'] = len(train_data.keys())
    intent_model_config['train']['epochs'] = 2
    print(intent_model_config)
    intent_model = train_model(intent_model_config)
    save(intent_model_config, intent_config_path)


def save(model_config, save_path):
    with open(save_path, 'w') as outfile:
        json.dump(model_config, outfile)


if __name__ == "__main__":
    train()
