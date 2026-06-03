# Contributing to ContextFlow

Thank you for your interest in contributing to ContextFlow! We welcome contributions of all kinds.

## How to Contribute

### Reporting Bugs

1. Check if the issue already exists
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python/Node version, etc.)

### Suggesting Features

1. Open an issue describing the feature
2. Explain the use case and benefits
3. Provide examples if possible

### Submitting Code

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Commit with clear messages: `git commit -m 'Add amazing feature'`
7. Push to your fork
8. Create a Pull Request

## Development Guidelines

### Code Style

**Python:**
- Follow PEP 8
- Use type hints
- Max line length: 100 characters
- Format with `black`: `black contextflow/`
- Lint with `flake8`: `flake8 contextflow/`

**TypeScript:**
- Use ESLint configuration provided
- Strict mode enabled
- Prettier formatting
- Run: `npm run lint` and `npm run format`

### Testing

- Write tests for all new code
- Aim for >80% coverage
- Run full test suite before submitting PR

### Documentation

- Update README.md for user-facing changes
- Add docstrings/JSDoc comments
- Update API documentation
- Include examples for new features

## Pull Request Process

1. Update documentation
2. Add/update tests
3. Ensure CI passes
4. Request review from maintainers
5. Address feedback
6. Squash commits if requested

## Code of Conduct

Please note we have a [Code of Conduct](./CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## Questions?

Feel free to open a discussion or reach out to maintainers.

Thanks for contributing! 🎉
