import { Action } from 'redux';
import { ThunkAction } from 'redux-thunk';
import { AppState } from '../store';
import { Blockchain } from '../services/blockchain';
import { Block } from '../services/blockchain/Block';
import { Transaction } from '../services/blockchain/Transaction';

export const ADD_BLOCK = 'ADD_BLOCK';
export const ADD_TRANSACTION = 'ADD_TRANSACTION';

export interface AddBlockAction extends Action {
  type: typeof ADD_BLOCK;
  block: Block;
}

export interface AddTransactionAction extends Action {
  type: typeof ADD_TRANSACTION;
  transaction: Transaction;
}

export type BlockchainActions = AddBlockAction | AddTransactionAction;

export const addBlock = (block: Block): ThunkAction<void, AppState, null, AddBlockAction> => {
  return async (dispatch, getState) => {
    const blockchain = getState().blockchain;
    blockchain.addBlock(block);
    dispatch({ type: ADD_BLOCK, block });
  };
};

export const addTransaction = (transaction: Transaction): ThunkAction<void, AppState, null, AddTransactionAction> => {
  return async (dispatch, getState) => {
    const blockchain = getState().blockchain;
    blockchain.addTransaction(transaction);
    dispatch({ type: ADD_TRANSACTION, transaction });
  };
};
