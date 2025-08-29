# Contributing to DataViz AI

We love your input! We want to make contributing to DataViz AI as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Pull Requests

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Any contributions you make will be under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using GitHub's [issue tracker](https://github.com/nicvazquezdev/dataviz-ai/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/nicvazquezdev/dataviz-ai/issues/new).

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People _love_ thorough bug reports. I'm not even kidding.

## Development Setup

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local frontend development)
- Python 3.9+ (for local backend development)
- Git

### Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/nicvazquezdev/dataviz-ai.git
   cd dataviz-ai
   ```

2. **Set up environment variables**

   ```bash
   cp .env.template .env
   # Edit .env with your OpenAI API key (optional - demo mode works without it)
   ```

3. **Start the development environment**

   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Local Development

#### Frontend Development

```bash
cd frontend
npm install
npm run dev
```

#### Backend Development

```bash
cd backend
pip install -r requirements.txt
python load_data.py
uvicorn app.main:app --reload
```

## Code Style

### Python (Backend)

- Follow PEP 8
- Use type hints where possible
- Write docstrings for functions and classes
- Use meaningful variable and function names

### TypeScript/JavaScript (Frontend)

- Use TypeScript for type safety
- Follow React best practices
- Use meaningful component and variable names
- Write JSDoc comments for complex functions

### General Guidelines

- Write clear, readable code
- Add comments for complex logic
- Keep functions small and focused
- Use meaningful commit messages

## Commit Message Convention

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
type(scope): description

[optional body]

[optional footer]
```

Types:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

Examples:

```
feat(backend): add support for CSV data upload
fix(frontend): resolve chart rendering issue on mobile
docs: update API documentation
```

## Testing

### Backend Tests

```bash
cd backend
python -m pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

## Code Review Process

1. All submissions require review
2. We may suggest changes, improvements, or alternatives
3. Changes must not break existing functionality
4. New features should include appropriate tests
5. Documentation should be updated for API changes

## Feature Requests

We welcome feature requests! Please:

1. Check if the feature already exists or is planned
2. Open an issue with the label "enhancement"
3. Describe the feature and its benefits
4. Include examples or mockups if applicable

## Questions?

Feel free to open an issue with the label "question" or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in our README.md file. Thank you for helping make DataViz AI better! 🎉
