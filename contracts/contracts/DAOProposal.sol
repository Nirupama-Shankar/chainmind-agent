// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract DAOProposal {

    struct Proposal {
        uint id;
        string description;
        uint voteCount;
    }

    uint public proposalCount;

    mapping(uint => Proposal) public proposals;

    function createProposal(string memory _description) public {
        proposalCount++;

        proposals[proposalCount] = Proposal(
            proposalCount,
            _description,
            0
        );
    }

    function vote(uint _proposalId) public {
        proposals[_proposalId].voteCount++;
    }
}