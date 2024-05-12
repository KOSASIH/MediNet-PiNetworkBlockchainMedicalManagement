// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Counters.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Strings.sol";

contract PiNetwork is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for string;

    // Mapping of medical records to their owners
    mapping(address => mapping(uint256 => MedicalRecord)) public medicalRecords;

    // Mapping of patients to their medical records
    mapping(address => uint256[]) public patientMedicalRecords;

    // Event emitted when a new medical record is created
    event NewMedicalRecord(address indexed patient, uint256 indexed medicalRecordId);

    // Event emitted when a medical record is updated
    event UpdateMedicalRecord(address indexed patient, uint256 indexed medicalRecordId);

    // Event emitted when a medical record is transferred
    event TransferMedicalRecord(address indexed from, address indexed to, uint256 indexed medicalRecordId);

    // Struct to represent a medical record
    struct MedicalRecord {
        uint256 id;
        string patientName;
        string diagnosis;
        string treatment;
        string medication;
        uint256 createdAt;
        uint256 updatedAt;
    }

    // Counter for medical record IDs
    Counters.Counter public medicalRecordIdCounter;

    // Modifier to restrict access to medical records
    modifier onlyPatientOrOwner(address patient, uint256 medicalRecordId) {
        require(
            msg.sender == patient || msg.sender == owner(),
            "Only the patient or the owner can access this medical record"
        );
        _;
    }

    // Constructor
    constructor() ERC721("PiNetwork", "PN") {
        // Initialize the medical record ID counter
        medicalRecordIdCounter = Counters.Counter(0);
    }

    // Create a new medical record
    function createMedicalRecord(
        address patient,
        string memory patientName,
        string memory diagnosis,
        string memory treatment,
        string memory medication
    ) public onlyOwner {
        // Generate a new medical record ID
        uint256 medicalRecordId = medicalRecordIdCounter.current();

        // Create a new medical record
        MedicalRecord storage medicalRecord = medicalRecords[patient][medicalRecordId];
        medicalRecord.id = medicalRecordId;
        medicalRecord.patientName = patientName;
        medicalRecord.diagnosis = diagnosis;
        medicalRecord.treatment = treatment;
        medicalRecord.medication = medication;
        medicalRecord.createdAt = block.timestamp;
        medicalRecord.updatedAt = block.timestamp;

        // Add the medical record to the patient's list
        patientMedicalRecords[patient].push(medicalRecordId);

        // Emit the NewMedicalRecord event
        emit NewMedicalRecord(patient, medicalRecordId);

        // Increment the medical record ID counter
        medicalRecordIdCounter.increment();
    }

    // Update a medical record
    function updateMedicalRecord(
        address patient,
        uint256 medicalRecordId,
        string memory diagnosis,
        string memory treatment,
        string memory medication
    ) public onlyPatientOrOwner(patient, medicalRecordId) {
        // Get the medical record
        MedicalRecord storage medicalRecord = medicalRecords[patient][medicalRecordId];

        // Update the medical record
        medicalRecord.diagnosis = diagnosis;
        medicalRecord.treatment = treatment;
        medicalRecord.medication = medication;
        medicalRecord.updatedAt = block.timestamp;

        // Emit the UpdateMedicalRecord event
        emit UpdateMedicalRecord(patient, medicalRecordId);
    }

    // Transfer a medical record
    function transferMedicalRecord(
        address from,
        address to,
        uint256 medicalRecordId
    ) public onlyPatientOrOwner(from, medicalRecordId) {
        // Get the medical record
        MedicalRecord storage medicalRecord = medicalRecords[from][medicalRecordId];

        // Remove the medical record from the from patient's list
        uint256 index = patientMedicalRecords[from].indexOf(medicalRecordId);
        patientMedicalRecords[from][index] = patientMedicalRecords[from][patientMedicalRecords[from].length - 1];
        patientMedicalRecords[from].pop();

        // Add the medical record to the to patient's list
        patientMedicalRecords[to].push(medicalRecordId);

        // Update the medical record owner
        medicalRecord.owner = to;

        // Emit the TransferMedicalRecord event
        emit TransferMedicalRecord(from, to, medicalRecordId);
    }

    // Get a medical record
    function getMedicalRecord(address patient, uint256 medicalRecordId) public view returns (MedicalRecord memory) {
        return medicalRecords[patient][medicalRecordId];
    }

    // Get a patient's medical records
    function getPatientMedicalRecords(address patient) public view returns (uint256[] memory) {
        return patientMedicalRecords[patient];
    }

    // Get the number of medical records
    function getMedicalRecordCount() public view returns (uint256) {
        return medicalRecordIdCounter.current();
    }
}
