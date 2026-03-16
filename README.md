# ChainMind
### AI Governance Agent for Decentralized DAOs

ChainMind is an AI-powered governance assistant designed to help Decentralized Autonomous Organizations (DAOs) respond to incidents and governance decisions more effectively.

The system analyzes DAO-related situations such as smart contract vulnerabilities, treasury decisions, or protocol upgrades, and generates structured governance proposals using AI. These proposals can then be stored on-chain using smart contracts, ensuring transparency and immutability.

This project was built for the **Gemini Live Agent Challenge**.

---

## Problem

DAOs often struggle to respond quickly when incidents occur in decentralized finance (DeFi) protocols. Security vulnerabilities, treasury allocations, or governance proposals require careful analysis before the community can take action.

The process of analyzing incidents and writing governance proposals can be slow and unstructured.

ChainMind explores how **AI agents can assist DAOs by generating governance recommendations automatically**.

---

## Solution

ChainMind introduces an **AI Governance Agent** that:

1. Accepts a description of a DAO situation
2. Uses AI to analyze the risk and context
3. Generates a governance proposal
4. Stores the proposal on-chain using a DAO smart contract
5. Displays all governance proposals in a simple dashboard

This creates a transparent and structured governance workflow.

---

## System Architecture

User Input  
↓  
AI Governance Agent (Gemini AI)  
↓  
Proposal Generation  
↓  
DAO Smart Contract  
↓  
On-Chain Proposal Storage  
↓  
Governance Dashboard

---

## Technologies Used

- Python (Flask)
- Google Gemini AI
- Web3.py
- Solidity Smart Contracts
- Hardhat
- HTML
- CSS
- JavaScript
- Ethereum Local Network

---

## Features

- AI-powered governance proposal generation
- Risk analysis and recommendation system
- Blockchain-based proposal storage
- DAO governance dashboard
- Smart contract integration

---

## Project Structure

chainmind-agent
│
├── backend
│ └── app.py
│
├── frontend
│ └── index.html
│
├── contracts
│ └── DAOProposal.sol
│
└── README.md

---

## How to Run the Project

### 1. Start Blockchain Network

cd contracts
npx hardhat node

---

### 2. Deploy Smart Contract

npx hardhat ignition deploy ignition/modules/DAOProposal.ts --network localhost

Copy the deployed contract address.

---

### 3. Start Backend Server

cd backend
source venv/bin/activate
python app.py

Backend runs at:

http://127.0.0.1:5000

---

### 4. Start Frontend

cd frontend
python3 -m http.server 5500

Open:

http://localhost:5500

---

## Demo Workflow

1. Enter a DAO scenario
2. Generate AI governance proposal
3. Submit proposal to blockchain
4. View proposals stored on-chain

---

## Example Demo Scenario

A vulnerability has been discovered in a DeFi protocol smart contract.
The DAO must decide whether to pause the protocol and conduct a security audit.

---

## Future Improvements

- DAO voting system
- Real-time DeFi risk monitoring
- Advanced AI risk scoring
- Voice interaction with the governance agent

---

## Author

Nirupama S  
PSG College of Technology

---

## Hackathon Submission

This project was created for the **Gemini Live Agent Challenge**, demonstrating how AI agents can assist decentralized governance systems.
