sudo apt install virtualenv
python3.6 -m venv faq_bot_venv
source faq_bot_venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m deeppavlov install intent_catcher
python train_and_save.py
