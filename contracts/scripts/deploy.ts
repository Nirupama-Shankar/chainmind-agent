import hre from "hardhat";

async function main() {

  const DAOProposal = await hre.ethers.getContractFactory("DAOProposal");

  const dao = await DAOProposal.deploy();

  await dao.waitForDeployment();

  console.log("DAOProposal deployed to:", await dao.getAddress());

}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});