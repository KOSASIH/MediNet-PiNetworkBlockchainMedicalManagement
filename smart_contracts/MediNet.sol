// MediNet.sol
pragma solidity ^0.8.10;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Counters.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Strings.sol";

contract MediNet is SafeERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for string;

    // Mapping of patient IDs to medical records
    mapping (address => mapping (uint256 => MedicalRecord)) public medicalRecords;

    // Mapping of doctor IDs to their medical specialties
    mapping (address => string[]) public doctorSpecialties;

    // Event emitted when a new medical record is created
    event NewMedicalRecord(address patient, uint256 recordId, string diagnosis);

    // Event emitted when a doctor updates a medical record
    event MedicalRecordUpdated(address doctor, uint256 recordId, string updatedDiagnosis);

    // Event emitted when a patient grants access to a doctor
    event AccessGranted(address patient, address doctor);

    // Event emitted when a patient revokes access from a doctor
    event AccessRevoked(address patient, address doctor);

    // Struct to represent a medical record
    struct MedicalRecord {
        uint256 id;
        string diagnosis;
        address[] doctorsWithAccess;
    }

    // Counter for medical record IDs
    Counters.Counter public medicalRecordIdCounter;

    // Modifier to restrict access to only the patient or authorized doctors
    modifier onlyAuthorized(address _patient, uint256 _recordId) {
        require(medicalRecords[_patient][_recordId].doctorsWithAccess.contains(msg.sender) || msg.sender == _patient, "Unauthorized access");
        _;
    }

    // Function to create a new medical record
    function createMedicalRecord(address _patient, string memory _diagnosis) public onlyOwner {
        medicalRecordIdCounter.increment();
        uint256 newRecordId = medicalRecordIdCounter.current();
        medicalRecords[_patient][newRecordId] = MedicalRecord(newRecordId, _diagnosis, new address[](0));
        emit NewMedicalRecord(_patient, newRecordId, _diagnosis);
    }

    // Function to update a medical record
    function updateMedicalRecord(address _patient, uint256 _recordId, string memory _updatedDiagnosis) public onlyAuthorized(_patient, _recordId) {
        medicalRecords[_patient][_recordId].diagnosis = _updatedDiagnosis;
        emit MedicalRecordUpdated(msg.sender, _recordId, _updatedDiagnosis);
    }

    // Function to grant access to a doctor
    function grantAccess(address _patient, address _doctor) public {
        require(msg.sender == _patient, "Only the patient can grant access");
        medicalRecords[_patient][medicalRecordIdCounter.current()].doctorsWithAccess.push(_doctor);
        emit AccessGranted(_patient, _doctor);
    }

    // Function to revoke access from a doctor
    function revokeAccess(address _patient, address _doctor) public {
        require(msg.sender == _patient, "Only the patient can revoke access");
        medicalRecords[_patient][medicalRecordIdCounter.current()].doctorsWithAccess.remove(_doctor);
        emit AccessRevoked(_patient, _doctor);
    }

    // Function to get a medical record by ID
    function getMedicalRecord(address _patient, uint256 _recordId) public view onlyAuthorized(_patient, _recordId) returns (MedicalRecord memory) {
        return medicalRecords[_patient][_recordId];
    }

    // Function to get all medical records for a patient
    function getMedicalRecords(address _patient) public view onlyAuthorized(_patient, 0) returns (MedicalRecord[] memory) {
        MedicalRecord[] memory records = new MedicalRecord[](medicalRecordIdCounter.current());
        for (uint256 i = 0; i < medicalRecordIdCounter.current(); i++) {
            records[i] = medicalRecords[_patient][i];
        }
        return records;
    }
}
