# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of DataViz AI seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Reporting Process

1. **DO NOT** create a public GitHub issue for the vulnerability.
2. **DO** include a detailed description of the vulnerability, including:
   - Type of issue (buffer overflow, SQL injection, cross-site scripting, etc.)
   - Full paths of source file(s) related to the vulnerability
   - The line number(s) of source file(s) related to the vulnerability
   - Any special configuration required to reproduce the issue
   - Step-by-step instructions to reproduce the issue
   - Proof-of-concept or exploit code (if possible)
   - Impact of the issue, including how an attacker might exploit it

### What to Expect

- You will receive an acknowledgment within 48 hours
- We will investigate and provide updates on our progress
- Once the issue is confirmed, we will work on a fix
- We will coordinate the disclosure with you
- We will credit you in our security advisory (unless you prefer to remain anonymous)

### Responsible Disclosure

We ask that you:

- Give us reasonable time to respond to issues before any disclosure to the public or a third-party
- Make a good faith effort to avoid privacy violations, destruction of data, and interruption or degradation of our service
- Not exploit a security issue you discover for any reason
- Not violate any other applicable laws or regulations

### Security Best Practices

When using DataViz AI, please follow these security best practices:

1. **Environment Variables**: Never commit API keys or sensitive credentials to version control
2. **Network Security**: Use HTTPS in production and secure your database connections
3. **Input Validation**: Always validate and sanitize user inputs
4. **Regular Updates**: Keep dependencies updated to the latest secure versions
5. **Access Control**: Implement proper authentication and authorization
6. **Monitoring**: Set up logging and monitoring for suspicious activities

### Known Security Considerations

- **OpenAI API Key**: The application requires an OpenAI API key for full functionality. Keep this key secure and never expose it in client-side code.
- **Database Credentials**: Database credentials should be stored securely and not committed to version control.
- **Demo Mode**: When running in demo mode, the application generates sample data and does not connect to external APIs.

### Security Updates

Security updates will be released as patch versions (e.g., 1.0.1, 1.0.2) and will be clearly marked in the changelog.

### Acknowledgments

We would like to thank all security researchers who responsibly disclose vulnerabilities to us. Your contributions help make DataViz AI more secure for everyone.

---

**Note**: This security policy is adapted from standard open source security practices. Please replace the placeholder contact information with your actual security contact details.
