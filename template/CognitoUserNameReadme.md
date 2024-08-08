# README for Cognito User Pool CloudFormation Template
## Overview

Setup-cognito with the following settings:

- **Sign-In Options**: Username and email
- **Password Policy**:
  - Minimum Length: 8 characters
  - Requires Numbers: 1
  - Requires Special Characters: 1
  - Requires Uppercase Letters: 1
  - Requires Lowercase Letters: 1
  - Password Validity Days: 30
- **Multi-Factor Authentication (MFA)**: Mandatory, using authentication apps
- **Account Recovery**: Enabled via email
- **Self-Registration**: Enabled
- **Email Configuration**: Default Cognito email provider

## Template Configuration

### Parameters

- **UserPoolName**: The name of the Cognito User Pool.
- **SmsConfiguration**:
  - **ExternalId**: The external ID used for role assumption.
  - **SnsCallerArn**: ARN of the IAM role used to send SMS messages.
- **EmailConfiguration**:
  - **EmailSendingAccount**: Set to `COGNITO_DEFAULT` for default email provider.


