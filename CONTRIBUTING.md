# Contributing Guidelines

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/ai-cofounder.git`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Install development dependencies: `pip install -r requirements.txt && pip install -r dev-requirements.txt`

## Development Workflow

### Code Style

We follow PEP 8 with some modifications:

```bash
# Format code with black
black app/ tests/

# Sort imports with isort
isort app/ tests/

# Lint with flake8
flake8 app/ tests/

# Type check with mypy
mypy app/
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_agents.py

# Run specific test
pytest tests/test_agents.py::test_strategic_agent_analysis
```

### Commit Messages

Follow conventional commits:

```
feat: Add strategic agent implementation
fix: Correct runway calculation
docs: Update API documentation
test: Add tests for financial agent
```

## Pull Request Process

1. Update the README.md with details of changes if applicable
2. Add tests for new functionality
3. Ensure all tests pass: `pytest`
4. Ensure code is formatted: `black app/`
5. Update documentation as needed
6. Submit PR with clear description of changes

## Code Review

All PRs require at least one approval before merging. Reviews should check:

- Code quality and style
- Test coverage
- Documentation
- Performance implications
- Security considerations

## Reporting Issues

Use GitHub issues for bugs and feature requests. Include:

- Clear description
- Steps to reproduce (for bugs)
- Expected behavior
- Actual behavior
- Python version and environment details

## Agent Development

When adding new agents:

1. Extend `BaseAgent` class
2. Implement `analyze()` method
3. Implement `recommend()` method
4. Add agent tests
5. Update coordinator if needed
6. Document agent capabilities

## Documentation

- Update docstrings for functions/classes
- Update README if adding major features
- Update API documentation
- Add architecture diagrams if needed

## Questions?

Open an issue or discussion for questions. The team is happy to help!
