# Matrix PiChain API Documentation

## Overview
The Matrix PiChain API provides a set of endpoints for interacting with the blockchain, managing wallets, and accessing analytics data.

## Base URL

https://api.matrixpichain.com/v1


## Authentication
All API requests require an API key. Include the API key in the request header:

Authorization: Bearer YOUR_API_KEY


## Endpoints

### 1. **Get Wallet Balance**
- **Endpoint**: `/wallet/balance`
- **Method**: GET
- **Description**: Retrieve the balance of a specified wallet.
- **Parameters**:
  - `address`: The wallet address to query.
- **Response**:
  ```json
  1 {
  2   "address": "string",
  3   "balance": "number"
  4 }
  ```

### 2. Create Transaction
- **Endpoint**: /transaction/create
- **Method**: POST
- **Description**: Create a new transaction.
- **Body**
 ```json
 1 {
 2   "from": "string",
 3   "to": "string",
 4   "amount": "number",
 5   "fee": "number"
 6 }
 ```

- **Response**
 ```json
 1 {
 2   "transaction_id": "string",
 3   "status": "string"
 4 }
 ```

### 3. Get Transaction History
- **Endpoint**: /wallet/history
- **Method**: GET
- **Description**: Retrieve the transaction history for a specified wallet.
- **Parameters**:
- **address**: The wallet address to query.
- **Response**:
 ```json
 1 {
 2   "transactions": [
 3     {
 4       "transaction_id": "string",
 5       "timestamp": "string",
 6       "amount": "number",
 7       "status": "string"
 8     }
 9   ]
 10 }
 ```

## Conclusion
This API documentation provides the necessary endpoints for developers to interact with the Matrix PiChain ecosystem. For further details, please refer to the individual endpoint descriptions.
