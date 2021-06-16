from deeppavlov import build_model


def infer(prediction_model, intent_model, query):
    out = prediction_model([query])
    intent = intent_model([query])
    answer = out[0][0]
    proba = max(out[1][0])
    return answer, proba, intent


def load(prediction_model_config_path='pred_model_config.json',
         intent_model_config_path='intent_model_config.json'):
    return build_model(prediction_model_config_path), \
           build_model(intent_model_config_path)
