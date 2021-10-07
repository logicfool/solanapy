import solana
import asyncio
from solana.rpc.api import Client
from solana import account
from utils import *
from solana.keypair import Keypair
from solana.rpc.commitment import Recent, Root


class solana_sniper():
    def __init__(self,rpc = "https://api.devnet.solana.com"):
        self.client = Client(rpc)
        self.config = load_config()['solana']
        self.keypair = Keypair.from_seed(get_seed_from_mnemonic(self.config['mnemonic']))
        self.account = account.Account(self.keypair)
        self.initializer_balance = self.client.get_balance(self.account.public_key(), commitment=Recent).get('result').get('value')

sol = solana_sniper()