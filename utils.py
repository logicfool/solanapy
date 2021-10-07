import base58
from bip_utils import Bip39SeedGenerator

#load config from config.ini
def load_config():
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_key_pair(secret_key):
    return 
    byte_array = base58.b58decode(secret_key)
    try:
        json_string = "[" + ",".join(map(lambda b: str(b), byte_array)) + "]"
    except:
        raise Exception("Error while generating keypair is this a correct secret_key?")
    print(json_string)



def get_seed_from_mnemonic(mnemonic):
    seed = Bip39SeedGenerator(mnemonic).Generate()
    return seed[0:32]