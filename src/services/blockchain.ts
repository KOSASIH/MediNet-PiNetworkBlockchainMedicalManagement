import { Block } from './Block';
import { Transaction } from './Transaction';
import { sha256 } from 'js-sha256';

export class Blockchain {
  private chain: Block[];
  private pendingTransactions: Transaction[];

  constructor() {
    this.chain = [this.createGenesisBlock()];
    this.pendingTransactions = [];
  }

  private createGenesisBlock(): Block {
    return new Block(0, Date.now(), 'Genesis Block', '0');
  }

  public getChain(): Block[] {
    return this.chain;
  }

  public getPendingTransactions(): Transaction[] {
    return this.pendingTransactions;
  }

  public addBlock(block: Block): void {
    block.previousHash = this.chain[this.chain.length - 1].hash;
    block.mineBlock();
    this.chain.push(block);
  }

  public addTransaction(transaction: Transaction): void {
    this.pendingTransactions.push(transaction);
  }

  public isChainValid(): boolean {
    for (let i = 1; i < this.chain.length; i++) {
      const currentBlock = this.chain[i];
      const previousBlock = this.chain[i - 1];

      if (currentBlock.hash !== currentBlock.calculateHash()) {
        return false;
      }

      if (currentBlock.previousHash !== previousBlock.hash) {
        return false;
      }
    }

    return true;
  }

  public replaceChain(newChain: Block[]): void {
    if (newChain.length < this.chain.length || !this.isChainValid()) {
      console.error('Received chain is invalid or shorter than the current chain.');
      return;
    }

    this.chain = newChain;
  }
}
