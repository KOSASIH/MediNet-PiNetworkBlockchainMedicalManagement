from web3 import Web3

def create_billing_contract(w3: Web3, contract_name: str, contract_bytecode: str, contract_abi: list) -> Web3.Contract:
    """
    Create a new real-time billing smart contract.

    Args:
        w3 (Web3): The Web3 instance.
        contract_name (str): The name of the smart contract.
        contract_bytecode (str): The bytecode of the smart contract.
        contract_abi (list): The ABI of the smart contract.

    Returns:
        Web3.Contract: The deployed real-time billing smart contract.
    """
    billing_contract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
    deployed_contract = billing_contract.constructor().transact({'from': w3.eth.defaultAccount})
    billing_contract = w3.eth.contract(address=deployed_contract.address, abi=contract_abi)

    return billing_contract

def add_product_to_billing(w3: Web3, billing_contract: Web3.Contract, product_id: int, price: int) -> None:
    """
    Add a new product to the real-time billing smart contract.

    Args:
        w3 (Web3): The Web3 instance.
        billing_contract (Web3.Contract): The real-time billing smart contract.
        product_id (int): The ID of the product.
        price (int): The price of the product.
    """
    billing_contract.functions.addProduct(product_id, price).transact({'from': w3.eth.defaultAccount})

def get_product_price(w3: Web3, billing_contract: Web3.Contract, product_id: int) -> int:
    """
    Get the price of a product in the real-time billing smart contract.

    Args:
        w3 (Web3): The Web3 instance.
        billing_contract (Web3.Contract): The real-time billing smart contract.
        product_id (int): The ID of the product.

    Returns:
        int: The price of the product.
    """
    return billing_contract.functions.getProductPrice(product_id).call()
