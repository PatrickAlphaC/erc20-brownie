pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract EasyToken is ERC20 {
    constructor() public ERC20("EasyToken", "EzT") {
        _mint(msg.sender, 1000000000000000000000000);
    }
}
