const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const dotenv = require('dotenv');
const { ethers } = require('ethers');
const { PatientContract, DoctorContract, MedicationContract } = require('./contracts');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Initialize Ethereum provider
const provider = new ethers.providers.InfuraProvider('mainnet', process.env.INFURA_API_KEY);

// Initialize contract instances
const patientContract = new PatientContract(provider, process.env.PATIENT_CONTRACT_ADDRESS);
const doctorContract = new DoctorContract(provider, process.env.DOCTOR_CONTRACT_ADDRESS);
const medicationContract = new MedicationContract(provider, process.env.MEDICATION_CONTRACT_ADDRESS);

// Routes
app.get('/', (req, res) => {
  res.send('Welcome to MediNet API!');
});

app.get('/patients', async (req, res) => {
  const patients = await patientContract.getAllPatients();
  res.json(patients);
});

app.post('/patients', async (req, res) => {
  const { name, dateOfBirth } = req.body;
  const tx = await patientContract.registerPatient(name, dateOfBirth);
  await tx.wait();
  res.status(201).send('Patient registered successfully');
});

app.get('/doctors', async (req, res) => {
  const doctors = await doctorContract.getAllDoctors();
  res.json(doctors);
});

app.post('/doctors', async (req, res) => {
  const { name, specialization } = req.body;
  const tx = await doctorContract.registerDoctor(name, specialization);
  await tx.wait();
  res.status(201).send('Doctor registered successfully');
});

app.get('/medications', async (req, res) => {
  const medications = await medicationContract.getAllMedications();
  res.json(medications);
});

app.post('/medications', async (req, res) => {
  const { name, manufacturer, dosage, instructions } = req.body;
  const tx = await medicationContract.registerMedication(name, manufacturer, dosage, instructions);
  await tx.wait();
  res.status(201).send('Medication registered successfully');
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
