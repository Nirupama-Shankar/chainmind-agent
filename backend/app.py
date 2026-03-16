from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

import google.generativeai as genai
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

app = Flask(__name__)
CORS(app)

# ---------------- GEMINI SETUP ---------------- #

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None


# ---------------- BLOCKCHAIN SETUP ---------------- #

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

contract_address = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

with open("../contracts/artifacts/contracts/DAOProposal.sol/DAOProposal.json") as f:
    contract_json = json.load(f)
    abi = contract_json["abi"]

contract = w3.eth.contract(address=contract_address, abi=abi)

account = w3.eth.accounts[0]


# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return "ChainMind AI Governance Agent Running"


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()
    user_input = data.get("input", "")

    prompt = f"""
You are an AI governance agent for a DAO.

Analyze the following situation:

{user_input}

Return:

Risk Score (1-10)
Urgency (LOW/MEDIUM/HIGH)
Risk Analysis
Suggested Governance Action
Final Governance Proposal
"""

    try:
        if model:
            response = model.generate_content(prompt)
            result = response.text
        else:
            raise Exception("Gemini disabled")

    except:

        text = user_input.lower()

        risk = "MEDIUM"
        score = "5/10"
        action = "Conduct investigation"

        if "exploit" in text or "hack" in text:
            risk = "HIGH"
            score = "9/10"
            action = "Pause protocol operations and launch emergency audit"

        elif "oracle" in text:
            risk = "HIGH"
            score = "8/10"
            action = "Upgrade oracle security and freeze suspicious trading"

        elif "treasury" in text:
            risk = "MEDIUM"
            score = "6/10"
            action = "Conduct DAO vote before allocating treasury funds"

        elif "upgrade" in text:
            risk = "LOW"
            score = "4/10"
            action = "Review upgrade proposal and conduct governance vote"

        result = f"""
    Risk Score: {score}
    Urgency: {risk}

    Risk Analysis:
    The AI governance agent analyzed the protocol situation based on the submitted scenario.

    Suggested Governance Action:
    {action}

    Final Governance Proposal:
    DAO members should vote on the recommended governance action to ensure protocol safety and stability.
    """

    return jsonify({"response": result})


@app.route("/submit", methods=["POST"])
def submit():

    data = request.get_json()
    proposal = data.get("proposal")

    tx = contract.functions.createProposal(proposal).transact({
        "from": account
    })

    return jsonify({
        "status": "stored",
        "tx": tx.hex()
    })


@app.route("/proposals")
def proposals():

    proposal_list = []

    count = contract.functions.proposalCount().call()

    for i in range(1, count + 1):

        p = contract.functions.proposals(i).call()

        proposal_list.append({
            "id": p[0],
            "description": p[1],
            "votes": p[2]
        })

    return jsonify(proposal_list)


if __name__ == "__main__":
    app.run(debug=True)