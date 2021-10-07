import base58
from bip_utils import Bip39SeedGenerator
import base58
import configparser
import os,json
class DotDict(dict):
    """
    a dictionary that supports dot notation 
    as well as dictionary access notation 
    usage: d = DotDict() or d = DotDict({'val1':'first'})
    set attributes: d.val2 = 'second' or d['val2'] = 'second'
    get attributes: d.val2 or d['val2']
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct):
        for key, value in dct.items():
            if hasattr(value, 'keys'):
                value = DotDict(value)
            self[key] = value


def load_config():
    """Load Config from file"""
    if os.path.exists('./config.ini'):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return DotDict(config)
    else:
        config = configparser.ConfigParser()
        config['solana'] = {'mnemonic':'','private_key':''}
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        print('Config created please edit the values to begin!')
        exit()
        # return DotDict(config)

def get_seed_from_private_key(private_key):
    """Get the seed to use with keypair from private key

    Args:
        private_key (str): Private key

    Returns:
        Seed (str): Seed to use with keypair
    """
    key_seed = base58.b58decode(private_key)
    return key_seed[:32]

def get_seed_from_mnemonic(mnemonic):
    seed = Bip39SeedGenerator(mnemonic).Generate()
    return seed[:32]

if __name__ == "__main__":
    config = load_config()['solana']