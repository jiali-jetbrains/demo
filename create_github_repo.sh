#!/bin/bash

echo "This script will help you create a GitHub repository called DemoJunieSnake and push your local repository to it."
echo "Please make sure you have a GitHub account and you're logged in."
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install git first."
    exit 1
fi

# Check if the current directory is a git repository
if [ ! -d .git ]; then
    echo "The current directory is not a git repository. Please run this script from the root of your project."
    exit 1
fi

echo "Step 1: Create a new repository on GitHub"
echo "1. Go to https://github.com/new"
echo "2. Name the repository 'DemoJunieSnake'"
echo "3. Leave it as a public repository"
echo "4. Do not initialize with README, .gitignore, or license (since we already have files)"
echo "5. Click 'Create repository'"
echo ""
echo "Press Enter when you've completed this step..."
read

echo "Step 2: Add the remote repository to your local repository"
echo "Enter your GitHub username:"
read username

git remote add origin "https://github.com/$username/DemoJunieSnake.git"
git branch -M main

echo "Step 3: Push your local repository to GitHub"
git push -u origin main

echo "Congratulations! Your project has been pushed to GitHub."
echo "You can view your repository at: https://github.com/$username/DemoJunieSnake"