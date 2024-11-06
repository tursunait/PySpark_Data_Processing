[![Rust CI/CD Pipeline](https://github.com/tursunait/Individual_Project_2_Tursunai_DE/actions/workflows/cicd.yml/badge.svg)](https://github.com/tursunait/Individual_Project_2_Tursunai_DE/actions/workflows/cicd.yml) 

# Urbanization Data CLI Tool
### By Tursunai Turumbekova
[Link To Demo Video](https://youtu.be/5NmfvoShtM0)

This Rust-based command-line tool extracts, transforms, and loads urbanization data into an SQLite database, allowing for CRUD (Create, Read, Update, Delete) operations. The project is set up with continuous integration and a structured `Makefile` for ease of use, with support for GitHub Actions CI/CD workflows. 

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Makefile Commands](#makefile-commands)
- [CI/CD Pipeline](#cicd-pipeline)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Features

1. **Data Extraction**: Downloads an urbanization dataset from a specified URL.
2. **Data Transformation & Loading**: Loads CSV data into an SQLite database.
3. **CRUD Operations**: Supports Create, Read, Update, and Delete operations on the database.
4. **Continuous Integration**: GitHub Actions workflow for CI/CD.
5. **Linting and Formatting**: Ensures code style and quality with Clippy and rustfmt.

## Setup

### Prerequisites

- **Rust** (latest stable version recommended)
- **SQLite** for database operations
- **Git** for version control
- **GitHub CLI** (optional, if using GitHub Actions locally)

### Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:tursunait/Individual_Project_2_Tursunai_DE.git
   cd Individual_Project_2_Tursunai_DE
   ```

2. **Install Rust**:
   - Install Rust using [rustup](https://rustup.rs/):
     ```bash
     curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
     ```

3. **Install Dependencies**:
   - Rust dependencies will be handled by `Cargo`, Rust's package manager, based on `Cargo.toml`.
   - Run the following command to build dependencies:
     ```bash
     cargo build
     ```

### Environment Variables
There are no environment variables required for this project.

## Usage

### Running the Program

To run the program, use the `make` commands for specific operations:

1. **Data Extraction**:
   ```bash
   make extract
   ```

2. **Load Data**:
   ```bash
   make load
   ```

3. **CRUD Operations**:
   - **Create** a record:
     ```bash
     make create
     ```
   - **Read** data:
     ```bash
     make read
     ```
   - **Update** a record:
     ```bash
     make update
     ```
   - **Delete** a record:
     ```bash
     make delete
     ```

4. **Run All Operations in Sequence**:
   ```bash
   make all
   ```

### Manual Run
Alternatively, you can run the program manually:
```bash
cargo run -- [extract|load|create|read|update|delete]
```

## File Structure

```
├── src
│   ├── main.rs              # Main entry point
│   ├── db_operations.rs     # Database operations (CRUD, loading data)
│   └── ...
├── data
│   └── urbanization.csv     # Data file (created during extraction)
├── Cargo.toml               # Project manifest
├── Makefile                 # Command automation
└── README.md                # Project documentation
```

## Makefile Commands

The `Makefile` provides several commands to automate tasks:

- **`make rust-version`**: Displays the versions of Rust utilities installed.
- **`make lint`**: Lints the code using Clippy.
- **`make test`**: Runs all tests.
- **`make release`**: Builds the project in release mode.
- **`make all`**: Runs formatting, linting, testing, and then executes the program.
- **`make [create|read|update|delete]`**: Performs specific CRUD operations.

## Interacting with CRUD Operations in the CLI

This project allows you to perform CRUD (Create, Read, Update, Delete) operations directly from the command line to manage city information in the SQLite database.

### Usage Examples

1. **Create a New Record**

  To add a new city record, use the `create` command followed by the necessary details:
  
  cargo run -- create <statefips> <state> <gisjoin> <lat_tract> <long_tract> <population> <adj_radiuspop_5> <urbanindex>

**Example:**
```bash
cargo run -- create "01" "Alabama" "G0100010" 34.0 -86.0 10000 200.0 0.8
```

2. **Read All Records**
  
  To display all city records stored in the database, use the read command:

**Example:**
```bash
cargo run -- read
```
  This command fetches and displays all entries from the database.

3. **Update an Existing Record**

  To update information for a specific city, use the update command along with the unique identifier (gisjoin) and the updated details:
  
  cargo run -- update <gisjoin> <state> <lat_tract> <long_tract> <population> <adj_radiuspop_5> <urbanindex>

**Example:**

```bash
    cargo run -- update "G0100010" "Alabama" 34.1 -86.1 10001 201.0 0.9
```

4. **Delete a Record**
  
  To delete a city record from the database, use the delete command with the unique identifier:
    cargo run -- delete <gisjoin>
**Example:**
```bash
cargo run -- delete "G0100010"
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration. The pipeline configuration (`cicd.yaml`) includes:

1. **Linting and Formatting**: Ensures the code meets style and quality guidelines.
2. **Build and Test**: Builds the project and runs tests.
3. **Artifact Upload**: Archives the optimized binary.

### GitHub Actions Workflow (cicd.yaml)
The GitHub Actions workflow automates the CI/CD process by running the following steps:

```yaml
name: Rust CI/CD Pipeline
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions-rs/toolchain@v1
        with:
          toolchain: stable
          components: clippy, rustfmt
      - name: Check Rust Versions
        run: make rust-version
      - name: Build Rust
        run: make release
      - name: Lint Code
        run: make lint
      - name: Run Tests
        run: make test
      - name: Archive Optimized Binary
        uses: actions/upload-artifact@v3
        with:
          name: optimized-binary
          path: target/release/urbanization_rs
```
## Optimized Rust Binary
The project generates an optimized Rust binary to ensure maximum performance. This binary is *compiled in release mode*, incorporating various compiler optimizations that improve runtime efficiency and reduce file size.

**Building the Optimized Binary**
The CI/CD pipeline in GitHub Actions automatically builds the optimized binary in release mode. This is done using the following command in the workflow:

```yaml
- name: Build Rust in Release Mode
  run: cargo build --release
``` 
This command produces the optimized binary, which is stored in the target/release directory.

**Downloading the Optimized Binary**
Once built, the optimized binary is archived as an artifact and can be downloaded directly from the GitHub Actions workflow run. This artifact is named *optimized-binary* and contains the urbanization_rs binary.

In the workflow, the binary is archived with the following step:

```yaml
- name: Archive Optimized Binary
  uses: actions/upload-artifact@v3
  with:
    name: optimized-binary
    path: target/release/urbanization_rs
```
This step ensures that every successful build produces an easily downloadable, production-ready binary.

## Dependencies

The primary dependencies for this project are:

- **`reqwest`**: Used for HTTP requests to download the CSV dataset.
- **`rusqlite`**: For interfacing with the SQLite database.
- **`csv`**: For reading and parsing CSV data.
  
These are managed through `Cargo.toml`.  Run `cargo build` to install them during setup.

## Using ChatGPT and GitHub Copilot
**ChatGPT**
Throughout this project, I used ChatGPT to troubleshoot issues, find best practices for Rust error handling, and optimize code structure. ChatGPT also assisted in clarifying Rust’s syntax and unique features, helping ensure that the project followed Rust’s idiomatic style.

**GitHub Copilot**
GitHub Copilot was instrumental in suggesting code snippets, especially for repetitive patterns and common Rust syntax. Copilot provided recommendations on structuring functions, handling errors effectively, and generating efficient Rust code for interacting with the SQLite database. These AI tools helped streamline the coding process and improved productivity.

## Contributing

1. Fork the project.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.
