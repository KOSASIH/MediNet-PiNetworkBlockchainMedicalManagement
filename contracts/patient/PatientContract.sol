pragma solidity ^0.8.10;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Counters.sol";
import "./PatientDataContract.sol";

contract PatientContract is Ownable, PatientDataContract {
    using Counters for Counters.Counter;

    // Mapping of patient IDs to patient data
    mapping (address => Patient) public patients;

    // Event emitted when a new patient is registered
    event PatientRegistered(address indexed patientAddress, uint256 patientId);

    // Event emitted when a patient's data is updated
    event PatientDataUpdated(address indexed patientAddress, uint256 patientId);

    // Counter for patient IDs
    Counters.Counter public patientIdCounter;

    /**
     * @dev Registers a new patient
     * @param _patientAddress The address of the patient
     * @param _name The name of the patient
     * @param _dateOfBirth The date of birth of the patient
     */
    function registerPatient(address _patientAddress, string memory _name, uint256 _dateOfBirth) public onlyOwner {
        // Generate a new patient ID
        uint256 patientId = patientIdCounter.current();
        patientIdCounter.increment();

        // Create a new patient struct
        Patient memory patient = Patient(_patientAddress, _name, _dateOfBirth, []);

        // Store the patient data
        patients[_patientAddress] = patient;

        // Emit the PatientRegistered event
        emit PatientRegistered(_patientAddress, patientId);
    }

    /**
     * @dev Updates a patient's data
     * @param _patientAddress The address of the patient
     * @param _name The new name of the patient
     * @param _dateOfBirth The new date of birth of the patient
     */
    function updatePatientData(address _patientAddress, string memory _name, uint256 _dateOfBirth) public onlyOwner {
        // Get the patient data
        Patient storage patient = patients[_patientAddress];

        // Update the patient data
        patient.name = _name;
        patient.dateOfBirth = _dateOfBirth;

        // Emit the PatientDataUpdated event
        emit PatientDataUpdated(_patientAddress, patient.id);
    }

    /**
     * @dev Gets a patient's data
     * @param _patientAddress The address of the patient
     * @return The patient's data
     */
    function getPatientData(address _patientAddress) public view returns (Patient memory) {
        return patients[_patientAddress];
    }
}
