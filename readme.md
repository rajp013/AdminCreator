# Web Application Backdoor Script

## Overview
This script enables an attacker to create a backdoor admin account and conceal it within a web application.

## Scenario
An attacker aims to gain unauthorized access to a web application by exploiting a vulnerability to create an admin account with a backdoor. The target web application features a userlisttable in its configuration page, which the attacker plans to manipulate.

## Usage
1. **Identify the Target Web Application**: Determine the base URL of the vulnerable web application.

2. **Run the Python Code**: Execute the provided Python script on your local machine, providing the target URL as an argument. This script will create an admin account with default credentials ("backdoor").

    ```bash
    python backdoor.py --url http://example.com/webapp
    ```

3. **Conceal the Backdoor Account**: The script will inject JavaScript code to hide the admin account from the userlisttable, ensuring it remains undetected.

4. **Access the Backdoor Account**: With the backdoor account created, the attacker can now log in to the web application and execute commands without raising suspicion.

## Example
Suppose the target web application is located at "http://example.com/webapp". To create a backdoor account, the attacker would execute the following command:

```bash
python backdoor.py --url http://example.com/webapp
```
## Additional Notes
- Ensure that you have proper authorization before attempting to execute this script.
- Use this script responsibly and for ethical purposes only.
- **Note**: This script is provided for educational purposes only. It is the responsibility of the user to ensure that they comply with all applicable laws and regulations when using this script. The creator of this script holds no responsibility for any misuse or illegal activities conducted with it.


