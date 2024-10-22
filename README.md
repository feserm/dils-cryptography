# DILS Seminar WiSe24/25 - Cryptography

## Description
This semester, we focus on cryptography. We begin with classical algorithms and basic techniques, trying to implement some by ourselves, following a book: "Implementing Cryptography Using Python" by Shannon W. Bray, 2020. Afterwards, we move on to more applied topics closer to our own research, e.g., encrypted databases.

## Installation

```bash
# Clone the repository
git clone https://github.com/feser/dils-cryptography.git

# Navigate to the project directory
cd dils-cryptography

# Install dependencies for Web UI
cd web
npm install

# Install dependencies for API
cd ../api
pip install -r requirements.txt
```

Prepare `api/.env` file

```
SECRET_KEY=<YOUR-SECRET-KEY>
```

To generate a secret key run:

```bash
openssl rand -hex 32
```

## Usage

```bash
# Start the application using Docker Compose
docker compose up -d
```

## Contributing
Guidelines for contributing to your project.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
