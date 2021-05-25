from deeppavlov import build_model


def infer(model, query):
    answer = model([query])[0][0]
    return answer

def load(config_path='model_config.json'):
    return build_model(config_path)
