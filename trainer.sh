sudo apt install virtualenv
virtualenv
python -m spacy download en_core_web_sm
pip install -r requirements.txt
python train_and_save.py
