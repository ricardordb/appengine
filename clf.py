from unicodedata import normalize as normtext
from joblib import load


removechars = '0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\t\n\r\x0b\x0c'
translation_names = str.maketrans('', '', removechars)


def clean_pfpj(name):
    name = normtext('NFKD', str(name)).encode('ASCII', 'ignore').decode('ASCII')
    name = name.translate(translation_names)
    name = name.title().strip()
    return name


clfpfpj = load("models/clfpfpj.joblib.gz")