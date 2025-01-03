1. **Install Node.js**
   Download and install Node.js from: [Node.js Official Website](https://nodejs.org/).

2. **Install Solana Web3.js Library**
   Install the Solana Web3.js library:
   ```bash
   npm install @solana/web3.js
   ```

3. **Solana CLI Setup**
   - Install Solana CLI tools:
     ```bash
     curl -sSf https://release.solana.com/stable/install > solana_install.sh && sh solana_install.sh
     ```
   - Set up Solana Devnet (or mainnet) for testing:
     ```bash
     solana config set --url https://api.devnet.solana.com
     ```

4. **Deploy Solana Program**
   Follow the `storage_program/instructions.md` to deploy your Solana program.
