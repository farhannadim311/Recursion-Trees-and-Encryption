# Python: Recursion, Trees, and Cryptography

This repository hosts a dual-module Python project demonstrating advanced algorithmic problem-solving and Object-Oriented software design. The project implements a recursive analysis engine for hierarchical tree structures and a robust, class-based system for One-Time Pad encryption.

## Project Overview

This codebase addresses two distinct challenges in computer science:
1.  **Data Structure Analysis**: Manipulating and verifying properties of tree-based data structures using recursive algorithms.
2.  **Secure Communication**: Modeling a cryptographic system to encrypt and decrypt messages using the One-Time Pad (OTP) cipher, theoretically known for its perfect secrecy.

## Key Features

### 1. Recursive Tree Analyzer
A module dedicated to efficient operations on custom tree nodes without relying on iterative loops.
* **Tree Height Calculation**: Implements a recursive Depth-First Search (DFS) strategy to determine the maximum depth of arbitrary tree structures.
* **Heap Property Verification**: A validator that recursively checks if a binary tree satisfies the Heap Property (Min-Heap or Max-Heap) given an arbitrary comparison function. This ensures data integrity for priority queue implementations.

### 2. One-Time Pad Encryption System
An Object-Oriented framework for secure message passing, utilizing inheritance to enforce clean separation of concerns between plaintext and ciphertext management.
* **Class Hierarchy**:
    * `Message`: Abstract base class defining common attributes and validation logic.
    * `PlaintextMessage`: Handles the encryption logic, shifting message characters against a random "pad" to produce secure ciphertext.
    * `EncryptedMessage`: Handles the decryption logic, reversing the specific pad shifts to recover original data.
* **Shift-Based Cryptography**: Implements modular arithmetic to handle character wrapping (A-Z, a-z) and preserves non-alphabetic characters during the encryption process.

## Technical Implementation

### Algorithms
* **Recursion**: Utilized extensively for tree traversal to maintain cleaner code and handle arbitrarily deep structures.
* **Complexity Management**: Optimized base cases to prevent stack overflow errors during deep tree analysis.

### Object-Oriented Design (OOD)
* **Inheritance**: Leveraged to share core functionality between message types, adhering to the "Don't Repeat Yourself" (DRY) principle.
* **Encapsulation**: Protected internal message states to ensure that a plaintext object cannot be accidentally mutated into an encrypted state without generating a new object instance.
* **Polymorphism**: Designed methods that behave contextually depending on whether the object represents raw data or encrypted content.

## Usage

### Prerequisites
* Python 3.x

### Running the Tree Analyzer
```python
# Example: Check if a tree is a Max Heap
root = Node(10, Node(5), Node(3))
is_valid = is_heap(root, lambda a, b: a > b)
print(f"Is Max Heap: {is_valid}")
```

### Encrypting a message
```python
pad = load_pad("pads.txt")
msg = PlaintextMessage("Hello World", pad)
encrypted_msg = msg.get_encrypted_message()

print(f"Original: {msg.get_text()}")
print(f"Encrypted: {encrypted_msg.get_text()}")
```
