pragma solidity ^0.8.10;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Counters.sol";
import "./DoctorDataContract.sol";

contract DoctorContract is Ownable, DoctorDataContract {
    using Counters for Counters.Counter;

    // Mapping of doctor IDs to doctor data
    mapping (address => Doctor) public doctors;

    // Event emitted when a new doctor is registered
    event DoctorRegistered(address indexed doctorAddress, uint256 doctorId);

    // Event emitted when a doctor's data is updated
    event DoctorDataUpdated(address indexed doctorAddress, uint256 doctorId);

    // Counter for doctor IDs
    Counters.Counter public doctorIdCounter;

    /**
     * @dev Registers a new doctor
     * @param _doctorAddress The address of the doctor
     * @param _name The name of the doctor
     * @param _specialization The specialization of the doctor
     */
    function registerDoctor(address _doctorAddress, string memory _name, string memory _specialization) public onlyOwner {
        // Generate a new doctor ID
        uint256 doctorId = doctorIdCounter.current();
        doctorIdCounter.increment();

        // Create a new doctor struct
        Doctor memory doctor = Doctor(_doctorAddress, _name, _specialization, []);

        // Store the doctor data
        doctors[_doctorAddress] = doctor;

        // Emit the DoctorRegistered event
        emit DoctorRegistered(_doctorAddress, doctorId);
    }

    /**
     * @dev Updates a doctor's data
     * @param _doctorAddress The address of the doctor
     * @param _name The new name of the doctor
     * @param _specialization The new specialization of the doctor
     */
    function updateDoctorData(address _doctorAddress, string memory _name, string memory _specialization) public onlyOwner {
        // Get the doctor data
        Doctor storage doctor = doctors[_doctorAddress];

        // Update the doctor data
        doctor.name = _name;
        doctor.specialization = _specialization;

        // Emit the DoctorDataUpdated event
        emit DoctorDataUpdated(_doctorAddress, doctor.id);
    }

    /**
     * @dev Gets a doctor's data
     * @param _doctorAddress The address of the doctor
     * @return The doctor's data
     */
    function getDoctorData(address _doctorAddress) public view returns (Doctor memory) {
        return doctors[_doctorAddress];
    }
}
