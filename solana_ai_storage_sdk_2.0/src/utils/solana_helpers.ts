import { Connection, Transaction } from "@solana/web3.js";

export async function sendTransaction(connection: Connection, transaction: Transaction, keypair: any): Promise<string> {
    const signature = await connection.sendTransaction(transaction, [keypair]);
    await connection.confirmTransaction(signature);
    return signature;
}
