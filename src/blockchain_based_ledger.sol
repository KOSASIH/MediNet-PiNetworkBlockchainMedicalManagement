pragma solidity ^0.8.0;

contract MedicalDataLedger {
    struct MedicalRecord {
        uint256 patientID;
        string medicalHistory;
        uint256[] sensorData;
    }

    mapping (address => MedicalRecord) public medicalRecords;

    function addMedicalRecord(uint256 _patientID, string _medicalHistory, uint256[] _sensorData) public {
        MedicalRecord storage medicalRecord = medicalRecords[msg.sender];
        medicalRecord.patientID = _patientID;
        medicalRecord.medicalHistory = _medicalHistory;
        medicalRecord.sensorData = _sensorData;
    }

    function getMedicalRecord(address _patientAddress) public view returns (MedicalRecord memory) {
        return medicalRecords[_patientAddress];
    }
}
