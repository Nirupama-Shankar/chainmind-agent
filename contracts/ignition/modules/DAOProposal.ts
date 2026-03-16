import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule("DAOProposalModule", (m) => {

  const daoProposal = m.contract("DAOProposal");

  return { daoProposal };

});