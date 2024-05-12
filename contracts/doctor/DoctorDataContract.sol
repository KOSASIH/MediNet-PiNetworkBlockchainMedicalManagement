pragma solidity ^0.8.10;

contract DoctorDataContract {
    struct Doctor {
        address doctorAddress;
        string name;
        string specialization;
        uint256[] medicalRecords; // Array of medical record IDs
    }
}
