# Motion Med Sync

## Overview

Motion Med Sync is a web application designed to help medical professionals synchronize and manage motion-related medical data. The application provides an intuitive interface for tracking, analyzing, and coordinating patient movement data.

## 🔗 Documentation

[Visit Motion Med Sync](https://markgustetic.github.io/Motion-Med-Sync)

## 🚀 Getting Started

### Installation

1. Install Python using Homebrew (macOS)

```bash
# Install Homebrew if you haven't already
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Verify installation
python3 --version
pip3 --version
```

2. Clone the repository

```bash
git clone https://github.com/markgustetic/Motion-Med-Sync.git
```

3. Create and activate a virtual environment

```bash
cd Motion-Med-Sync
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
```

### Updating Files

1. Check out the latest repo
2. Create a new branch
3. Edit the files in the data folder. Do not edit the files in the root folder.
4. Run the conversion script
5. Commit and push the changes
6. Create a pull request

### Run the conversion script

```bash
python3 update_html.py
```
