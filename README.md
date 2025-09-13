# Python Web Application with CI/CD Pipeline

A Flask-based web application with comprehensive CI/CD pipeline using GitHub Actions.

## Project Structure

```
.
├── app.py                 # Main Flask application
├── test_app.py           # Unit tests
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
└── .github/workflows    # CI/CD pipeline configurations
```

## Technical Stack

- Python 3.12
- Flask Web Framework
- pytest for Unit Testing
- Docker for Containerization
- GitHub Actions for CI/CD
- Ruff for Code Linting
- CodeQL for Security Analysis
- Trivy for Container Scanning

## Getting Started

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/<username>/python-webapp.git
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## CI/CD Pipeline Steps

### 1. Code Linting
- Uses [Ruff](https://github.com/astral-sh/ruff) for Python code linting
- Automatically fixes formatting issues
```yaml
- name: ruff-action
  uses: astral-sh/ruff-action@v3.5.1
```

### 2. Secret Scanning
- Implements Gitleaks for detecting hardcoded secrets
- Runs on pull requests and scheduled scans
- Reference: [Gitleaks Documentation](https://github.com/gitleaks/gitleaks)

### 3. Code Scanning
- Uses CodeQL for security vulnerability analysis
- Supports multiple languages (Python and GitHub Actions)
- Reference: [CodeQL Documentation](https://codeql.github.com/docs/)

### 4. Unit Testing
- Implements pytest for automated testing
- Uses matrix strategy for multiple Python versions
- Challenge Faced: ModuleNotFoundError
- Solution: Ensure proper Python path configuration in CI environment

### 5. Docker Build & Security
- Builds container image
- Implements Trivy for vulnerability scanning
- Pushes image to Docker Hub
- Reference: [Trivy Documentation](https://aquasecurity.github.io/trivy/)

### 6. Deployment
- Automated container deployment
- Health check implementation
- Email notifications for deployment status

## Challenges Faced & Solutions

### 1. Module Import Error
**Challenge**: Test failures due to module import issues
```
ModuleNotFoundError: No module named 'app'
```
**Solution**: 
- Ensure proper directory structure
- Add `__init__.py` files
- Configure PYTHONPATH in CI environment

### 2. Email Notifications
**Challenge**: Gmail SMTP authentication failures
**Solution**: 
- Use App-specific passwords
- Configure proper SMTP settings
- Alternative: Use GitHub notification settings

### 3. Docker Security
**Challenge**: Container vulnerabilities
**Solution**: 
- Implement Trivy scanning
- Use minimal base images
- Regular dependency updates with Dependabot

## Security Features

1. Automated Dependency Updates
```yaml
- package-ecosystem: "pip"
  directory: "/"
  schedule:
    interval: "weekly"
```


## Monitoring & Alerts

```yaml
- name: Monitor Application Status
  run: |
    for i in {1..5}; do
      health_status=$(curl -s http://localhost:5000/health)
      echo "Health Check $i: $health_status"
      sleep 10
    done
```

## Useful Commands

```bash
# Check deployment status
curl -I http://localhost:5000/health

# View logs
tail -f logs/application.log

# Monitor resources
top -b -n 1

# Check running processes
ps aux | grep python
```


2. CodeQL Analysis
- Security vulnerability scanning
- Code quality checks
- Regular scheduled scans

3. Container Security
- Base image scanning
- Dependency vulnerability checks
- Runtime security controls

## Useful References

1. [Flask Documentation](https://flask.palletsprojects.com/)
2. [GitHub Actions Documentation](https://docs.github.com/en/actions)
3. [pytest Documentation](https://docs.pytest.org/)
4. [Docker Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
5. [GitHub Security Features](https://docs.github.com/en/code-security)
6. [Python Security Best Practices](https://python-security.readthedocs.io/)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.


