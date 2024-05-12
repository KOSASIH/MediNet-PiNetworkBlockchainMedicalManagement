import { BlockchainService } from './blockchain';

describe('BlockchainService', () => {
  let blockchainService: BlockchainService;

  beforeEach(() => {
    blockchainService = new BlockchainService();
  });

  it('should create a new blockchain', async () => {
    const blockchain = await blockchainService.createBlockchain();
    expect(blockchain).toBeDefined();
    expect(blockchain.chain.length).toBeGreaterThan(0);
  });

  it('should add a new block to the blockchain', async () => {
    const blockchain = await blockchainService.createBlockchain();
    const newBlock = await blockchainService.addBlock(blockchain, { data: 'Test data' });
    expect(newBlock).toBeDefined();
    expect(newBlock.index).toBeGreaterThan(blockchain.chain.length);
  });

  it('should validate the blockchain', async () => {
    const blockchain = await blockchainService.createBlockchain();
    const isValid = await blockchainService.validateBlockchain(blockchain);
    expect(isValid).toBe(true);
  });
});
