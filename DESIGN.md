# Design Doc: File Organizer CLI

## Overview

This project implements a command-line tool that organizes files in a user-specified folder. The tool supports organizing by:
- File type
- Last modified date
- Keyword in filename

The goal is to automate organization while keeping the interface simple.

## Problem

Folders such as Downloads often become cluttered with many different file types. Manually sorting files is repetitive and time-consuming.

## Goals

- Build a simple command-line interface.
- Organize files using one of three methods.
- Work on any folder specified by the user.
- Keep the implementation easy to extend.

## Non-Goals

- GUI application
- Recursive organization of subfolders
- Undo/history functionality
- Cloud synchronization

## Proposed Design

The application consists of three main parts:

1. Read user input (folder path and organization mode).
2. Scan the directory for files.
3. Move files into appropriate locations based on the selected mode.

Each organization strategy will be implemented as its own function.

## Alternatives Considered

### Single large function

Pros:
- Quick to write.

Cons:
- Harder to maintain and extend.

Decision:
Separate each organization strategy into its own function.

### Organize by extension vs. broad categories

Organizing by extension (pdf, png, txt) is simpler and requires less manual mapping than maintaining categories like Documents or Images.

Decision:
Use file extensions.

## Risks

- Accidentally moving files unexpectedly.
- Filename collisions if two files with the same name exist.

These are acceptable limitations for the first version.

## Future Improvements

- Preview mode (show changes before moving files).
- Undo support.
- Recursive directory organization.
- Configuration file for custom categories.