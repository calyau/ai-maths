---
# === CORE IDENTIFICATION ===
concept: Affine Cryptosystem
slug: affine-cryptosystem

# === CLASSIFICATION ===
category: applications-crypto
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Introduction to Cryptography"
chapter_number: 7
pdf_page: 96
section: "7.1 Private Key Cryptography"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - private-key-cryptography
extends:
  - monoalphabetic-cryptosystem
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an affine cryptosystem?"
  - "When does an affine cipher have a valid decryption function?"
---

# Quick Definition

An affine cryptosystem encrypts using $f(p) = ap + b \bmod 26$, where $\gcd(a, 26) = 1$. Decryption is $f^{-1}(p) = a^{-1}p - a^{-1}b \bmod 26$. The condition on $a$ ensures the cipher is invertible.

# Core Definition

"Such a cryptosystem is called an *affine cryptosystem*" (Judson, p. 96). The encoding function is $f(p) = ap + b \bmod 26$, which has a decoding function $f^{-1}(p) = a^{-1}p - a^{-1}b \bmod 26$ exactly when $\gcd(a, 26) = 1$ (i.e., $a$ is invertible in $\mathbb{Z}_{26}$).

# Prerequisites

- **Private Key Cryptography** — An affine cipher is a private key system

# Key Properties

1. Encryption: $f(p) = ap + b \bmod 26$
2. Decryption: $f^{-1}(p) = a^{-1}(p - b) \bmod 26$
3. Requires $\gcd(a, 26) = 1$ for the cipher to be invertible
4. When $a = 1$, reduces to a simple shift cipher
5. Still a monoalphabetic cipher and vulnerable to frequency analysis

# Construction / Recognition

## To Set Up:
1. Choose $a$ with $\gcd(a, 26) = 1$ and any $b \in \mathbb{Z}_{26}$
2. Compute $a^{-1}$ in $\mathbb{Z}_{26}$
3. Encrypt: $f(p) = ap + b \bmod 26$
4. Decrypt: $f^{-1}(c) = a^{-1}(c - b) \bmod 26$

# Context & Application

The affine cipher is a natural generalization of the shift cipher that uses the group of units $U(26)$. It illustrates the connection between invertibility in modular arithmetic and cryptographic security.

# Examples

**Example 1** (p. 96): With $a = 5$, $b = 3$: $a^{-1} = 21$ since $5 \cdot 21 = 105 \equiv 1 \pmod{26}$. Encryption: $f(p) = 5p + 3 \bmod 26$. "ALGEBRA" encodes as "DGHXIKD". Decryption: $f^{-1}(p) = 21p + 15 \bmod 26$.

# Relationships

## Builds Upon
- **Private Key Cryptography** — An affine cipher is a private key system
- **Monoalphabetic Cryptosystem** — The affine cipher is monoalphabetic

## Related
- **Group of Units** — Requires $a \in U(26)$

# Common Errors

- **Error**: Choosing $a$ with $\gcd(a, 26) \neq 1$
  **Correction**: The cipher is only invertible when $a$ is a unit in $\mathbb{Z}_{26}$

# Common Confusions

- **Confusion**: Thinking the affine cipher is significantly more secure than a shift cipher
  **Clarification**: It has more keys but is still monoalphabetic and breakable by frequency analysis

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.1, Example 7.3, page 96.

# Verification Notes

- Definition source: Direct from p. 96
- Confidence rationale: Explicit definition and example
- Uncertainties: None
- Cross-reference status: Verified
