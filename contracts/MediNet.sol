pragma solidity ^0.8.0;

import "./Prescription.sol";
import "./MedicalSupply.sol";

contract MediNet {
    Prescription[] public prescriptions;
    MedicalSupply[] public medicalSupplies;

    event PrescriptionCreated(uint256 indexed prescriptionId);
    event MedicalSupplyCreated(uint256 indexed medicalSupplyId);

    function createPrescription(uint256 patientId, string memory drugName, uint256 drugDosage, uint256 drugFrequency) public {
        Prescription memory newPrescription = new Prescription(patientId, drugName, drugDosage, drugFrequency);
        prescriptions.push(newPrescription);
        emit PrescriptionCreated(newPrescription.id());
    }

    function getPrescription(uint256 prescriptionId) public view returns (uint256, string memory, uint256, uint256) {
        Prescription memory prescription = prescriptions[prescriptionId];
        return (prescription.patientId(), prescription.drugName(), prescription.drugDosage(), prescription.drugFrequency());
    }

    function createMedicalSupply(string memory name, uint256 quantity) public {
        MedicalSupply memory newMedicalSupply = new MedicalSupply(name, quantity);
        medicalSupplies.push(newMedicalSupply);
        emit MedicalSupplyCreated(newMedicalSupply.id());
    }

    function getMedicalSupply(uint256 medicalSupplyId) public view returns (string memory, uint256) {
        MedicalSupply memory medicalSupply = medicalSupplies[medicalSupplyId];
        return (medicalSupply.name(), medicalSupply.quantity());
    }
}
