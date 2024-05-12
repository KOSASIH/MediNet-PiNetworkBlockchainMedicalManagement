pragma solidity ^0.8.10;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/access/Ownable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/utils/Counters.sol";
import "./MedicationDataContract.sol";

contract MedicationContract is Ownable, MedicationDataContract {
    using Counters for Counters.Counter;

    // Mapping of medication IDs to medication data
    mapping (bytes32 => Medication) public medications;

    // Event emitted when a new medication is registered
    event MedicationRegistered(bytes32 indexed medicationId);

    // Event emitted when a medication's data is updated
    event MedicationDataUpdated(bytes32 indexed medicationId);

    // Counter for medication IDs
    Counters.Counter public medicationIdCounter;

    /**
     * @dev Registers a new medication
     * @param _medication The medication data
     */
    function registerMedication(Medication memory _medication) public onlyOwner {
        // Generate a new medication ID
        bytes32 medicationId = keccak256(abi.encodePacked(medicationIdCounter.current()));
        medicationIdCounter.increment();

        // Store the medication data
        medications[medicationId] = _medication;

        // Emit the MedicationRegistered event
        emit MedicationRegistered(medicationId);
    }

    /**
     * @dev Updates a medication's data
     * @param _medicationId The ID of the medication
     * @param _medication The new medication data
     */
    function updateMedicationData(bytes32 _medicationId, Medication memory _medication) public onlyOwner {
        // Get the medication data
        Medication storage medication = medications[_medicationId];

        // Update the medication data
        medication = _medication;

        // Emit the MedicationDataUpdated event
        emit MedicationDataUpdated(_medicationId);
    }

    /**
     * @dev Gets a medication's data
     * @param _medicationId The ID of the medication
     * @return The medication's data
     */
    function getMedicationData(bytes32 _medicationId) public view returns (Medication memory) {
        return medications[_medicationId];
    }
}
