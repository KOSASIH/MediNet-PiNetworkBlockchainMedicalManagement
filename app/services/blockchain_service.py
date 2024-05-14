import json
from web3 import Web3
from solcx import compile_source

class BlockchainService:
    def __init__(self, contract_abi, contract_address, web3_provider):
        self.contract_abi = contract_abi
        self.contract_address = contract_address
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    def call_contract_method(self, method_name, *args):
        method = self.contract.functions[method_name](*args)
        return method.call()

    def send_transaction(self, method_name, *args, gas=None, gas_price=None):
        method = self.contract.functions[method_name](*args)
        if gas and gas_price:
            transaction = method.buildTransaction({'gas': gas, 'gasPrice': gas_price})
        else:
            transaction = method.buildTransaction({'gas': method.estimateGas()})
        signed_transaction = self.web3.eth.account.signTransaction(transaction, private_key='your_private_key')
        return self.web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    def deploy_contract(self, contract_source, constructor_args, gas=None, gas_price=None):
        compiled_sol = compile_source(contract_source)
        contract_id, contract_interface = compiled_sol.popitem()
        contract_bytecode = contract_interface['bin']
        contract_constructor = contract_interface['abi'][0]
        if gas and gas_price:
            transaction = self.web3.eth.contract(abi=contract_interface['abi']).constructor(*constructor_args).buildTransaction({'gas': gas, 'gasPrice': gas_price})
        else:
            transaction = self.web3.eth.contract(abi=contract_interface['abi']).constructor(*constructor_args).buildTransaction({'gas': transaction.estimateGas()})
        signed_transaction = self.web3.eth.account.signTransaction(transaction, private_key='your_private_key')
        receipt = self.web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        contract_address = self.web3.eth.getTransactionReceipt(receipt)['contractAddress']
        return self.web3.eth.contract(address=contract_address, abi=contract_interface['abi'])
