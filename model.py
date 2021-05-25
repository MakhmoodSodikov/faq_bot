from deeppavlov import build_model


def infer(model, query):
    out = model([query])
    answer = out[0][0]
    proba = max(out[1][0])
    return answer, proba


def load(config_path='model_config.json'):
    return build_model(config_path)
