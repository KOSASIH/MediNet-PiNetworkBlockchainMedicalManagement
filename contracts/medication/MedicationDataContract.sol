pragma solidity ^0.8.10;

contract MedicationDataContract {
    struct Medication {
        string name;
        string manufacturer;
        uint256 dosage;
        string instructions;
    }
}
