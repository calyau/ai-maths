---
# === CORE IDENTIFICATION ===
concept: Polyalphabetic Cryptosystem
slug: polyalphabetic-cryptosystem

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
extends: []
related:
  - affine-cryptosystem
contrasts_with:
  - monoalphabetic-cryptosystem

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a polyalphabetic cryptosystem?"
  - "How does matrix encryption work?"
---

# Quick Definition

A polyalphabetic cryptosystem is one where a ciphertext letter can represent more than one plaintext letter. The text uses matrix-based encryption on pairs (or blocks) of letters to achieve this.

# Core Definition

A polyalphabetic cryptosystem encodes pairs (or blocks) of letters using an invertible matrix $A$ over $\mathbb{Z}_{26}$: $f(\mathbf{p}) = A\mathbf{p} + \mathbf{b}$, with decryption $f^{-1}(\mathbf{p}) = A^{-1}\mathbf{p} - A^{-1}\mathbf{b}$ (Judson, p. 96). This makes "a ciphertext letter could represent more than one plaintext letter."

# Prerequisites

- **Private Key Cryptography** — A polyalphabetic cipher is a private key system

# Key Properties

1. A single ciphertext letter can represent multiple plaintext letters
2. Uses matrix operations over $\mathbb{Z}_{26}$
3. Requires the matrix $A$ to be invertible (i.e., $\gcd(\det(A), 26) = 1$)
4. More resistant to frequency analysis than monoalphabetic systems
5. Larger matrices increase security

# Construction / Recognition

## To Set Up:
1. Choose an invertible $2 \times 2$ (or larger) matrix $A$ with entries in $\mathbb{Z}_{26}$
2. Choose a vector $\mathbf{b}$
3. Encrypt pairs: $f(\mathbf{p}) = A\mathbf{p} + \mathbf{b} \bmod 26$
4. Decrypt: $f^{-1}(\mathbf{c}) = A^{-1}(\mathbf{c} - \mathbf{b}) \bmod 26$

# Context & Application

Polyalphabetic ciphers are more secure than monoalphabetic ones because the same plaintext letter can encrypt to different ciphertext letters depending on its pairing. Frequency analysis on pairs is still possible but requires more data.

# Examples

**Example 1** (p. 96): Encode "HELP" (7, 4, 11, 15) with $A = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$, $\mathbf{b} = (2, 2)^t$. Processing pairs: $(7, 4)^t$ and $(11, 15)^t$. The encrypted message is "RRGR". Note that R represents more than one plaintext letter.

# Relationships

## Builds Upon
- **Private Key Cryptography** — A type of private key system

## Contrasts With
- **Monoalphabetic Cryptosystem** — Where each ciphertext letter represents exactly one plaintext letter

# Common Errors

- **Error**: Using a non-invertible matrix
  **Correction**: Must have $\gcd(\det(A), 26) = 1$

# Common Confusions

- **Confusion**: Thinking polyalphabetic ciphers are unbreakable
  **Clarification**: Frequency analysis on pairs/blocks can still break them; larger block sizes help

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.1, Example 7.4, page 96.

# Verification Notes

- Definition source: Direct from p. 96
- Confidence rationale: Explicit definition with example
- Uncertainties: None
- Cross-reference status: Verified
