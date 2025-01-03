import { Connection, PublicKey, Transaction, SystemProgram } from "@solana/web3.js";
import { sendTransaction } from './utils/solana_helpers';

const connection = new Connection("https://api.devnet.solana.com");
const programId = new PublicKey("YOUR_PROGRAM_ID");  // Replace with your deployed program ID

async function storeFileMetadata(fileHash: string) {
    const transaction = new Transaction().add(
        SystemProgram.transfer({
            fromPubkey: YOUR_WALLET_PUBLIC_KEY,
            toPubkey: programId,
            lamports: 1000,  // Example fee for file registration
        })
    );

    const signature = await sendTransaction(connection, transaction, YOUR_WALLET_KEYPAIR);
    console.log("Transaction sent:", signature);
}
