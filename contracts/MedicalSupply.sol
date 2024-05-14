pragma solidity ^0.8.0;

contract MedicalSupply {
    uint256 private id;
    string private name;
    uint256 private quantity;

    constructor(string memory _name, uint256 _quantity) {
        id = hash(_name, _quantity);
        name = _name;
        quantity = _quantity;
    }

    function id() public view returns (uint256) {
        return id;
    }

    function name() public view returns (string memory) {
        return name;
    }

    function quantity() public view returns (uint256) {
        return quantity;
    }

    function hash(string memory _name, uint256 _quantity) private pure returns (uint256) {
        return keccak256(abi.encodePacked(_name, _quantity));
    }
}
