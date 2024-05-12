from web3 import Web3

def create_supply_chain_contract(w3: Web3, contract_name: str, contract_bytecode: str, contract_abi: list) -> Web3.Contract:
    """
    Create a new supply chain management smart contract.

    Args:
        w3 (Web3): The Web3 instance.
        contract_name (str): The name of the smart contract.
        contract_bytecode (str): The bytecode of the smart contract.
        contract_abi (list): The ABI of the smart contract.

    Returns:
        Web3.Contract: The deployed supply chain management smart contract.
    """
    supply_chain_contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    deployed_contract = supply_chain_contract.constructor().transact({'from': w3.eth.defaultAccount})
    supply_chain_contract = w3.eth.contract(address=deployed_contract.address, abi=contract_abi)

    return supply_chain_contract

def add_product_to_supply_chain(w3: Web3, supply_chain_contract: Web3.Contract, product_id: int, manufacturer: str, timestamp: int) -> None:
    """
    Add a new product to the supply chain.

    Args:
        w3 (Web3): The Web3 instance.
        supply_chain_contract (Web3.Contract): The supply chain management smart contract.
        product_id (int): The ID of the product.
        manufacturer (str): The name of the manufacturer.
        timestamp (int): The timestamp of the transaction.
    """
    supply_chain_contract.functions.addProduct(product_id, manufacturer, timestamp).transact({'from': w3.eth.defaultAccount})

def update_product_location(w3: Web3, supply_chain_contract: Web3.Contract, product_id: int, new_location: str) -> None:
    """
    Update the location of a product in the supply chain.

    Args:
        w3 (Web3): The Web3 instance.
        supply_chain_contract (Web3.Contract): The supply chain management smart contract.
        product_id (int): The ID of the product.
        new_location (str): The new location of the product.
    """
    supply_chain_contract.functions.updateProductLocation(product_id, new_location).transact({'from': w3.eth.defaultAccount})

def get_product_location(w3: Web3, supply_chain_contract: Web3.Contract, product_id: int) -> str:
    """
    Get the current location of a product in the supply chain.

    Args:
        w3 (Web3): The Web3 instance.
        supply_chain_contract (Web3.Contract): The supply chain management smart contract.
        product_id (int): The ID of the product.

    Returns:
        str: The current location of the product.
    """
    return supply_chain_contract.functions.getProductLocation(product_id).call()
