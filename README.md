# Pharmacy Billing System

## Overview
This Python program is a simple pharmacy billing system that allows customers to:
1. Enter their phone number to identify themselves.
2. Add medicines to their bill by selecting from a predefined list.
3. Calculate the total bill based on medicine prices and quantities.
4. Earn loyalty points on their purchases.
5. Redeem loyalty points to reduce their bill amount in future transactions.

## Features
- **Phone Number Validation**: Ensures the phone number entered is a valid 10-digit number.
- **Medicine Selection**: Customers can choose medicines from a predefined list with fixed prices.
- **Billing Calculation**: Calculates the total bill based on the selected medicines and their quantities.
- **Loyalty Points System**: Accumulates points based on the total bill and allows customers to redeem them.
- **Point Redemption**: Customers can choose how many points they wish to redeem to reduce their bill amount.

## Usage Instructions

### Initial Setup
1. Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the directory:
   ```bash
   cd pharmacy-billing-system
   ```
3. Ensure Python 3.x is installed on your system.
4. Run the script:
   ```bash
   python billing_system.py
   ```

### Workflow
1. Enter your phone number when prompted. The program validates if it’s a 10-digit number.
2. Specify the number of medicines you want to purchase. If the number is zero, the program will prompt you to enter a valid value.
3. Add medicines by entering their name and quantity. The program calculates the total bill.
4. The program awards loyalty points based on your total bill (1 point for every 100 units of currency spent).
5. If you return with the same phone number, you can redeem your points to reduce the total bill amount.
6. If points are redeemed, the program adjusts the net payable amount and updates the loyalty points balance.

### Example
1. Enter phone number:
   ```
   enter the no. 1234567890
   ```
2. Number of medicines to purchase:
   ```
   enter the number of medicine:- 2
   ```
3. Add medicines:
   ```
   enter the medicine:- A
   enter the quantity:- 3
   enter the medicine:- B
   enter the quantity:- 2
   ```
4. Output:
   ```
   Total pay amount:- 70
   Available points: 0
   ```
5. Redeem points:
   ```
   Do you want to Redeem point:- Yes
   how many points you want to redeem, you have balance point is 0
   ```
6. Final output:
   ```
   Net amount to be paid after point redemption: 70
   Balance points: 0
   ```

## Code Structure
- **List_of_medicine**: A dictionary containing medicines and their prices.
- **global_sum**: Keeps track of the total bill across multiple transactions.
- **Loyalty Points**: Points are calculated as `total bill / 100`, and each point is worth 10 units of currency.

## Known Limitations
- Case-sensitive medicine names.
- Assumes input is always valid; no error handling for incorrect data types.
- No database for storing loyalty points between runs.

## Future Enhancements
- Add a database to store customer data and loyalty points persistently.
- Implement a user-friendly GUI.
- Include error handling for invalid inputs.

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request. Any suggestions or contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

