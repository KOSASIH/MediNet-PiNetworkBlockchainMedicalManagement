pragma solidity ^0.8.10;

contract PatientDataContract {
    struct Patient {
        address patientAddress;
        string name;
        uint256 dateOfBirth;
        uint256[] medicalRecords; // Array of medical record IDs
    }
}
