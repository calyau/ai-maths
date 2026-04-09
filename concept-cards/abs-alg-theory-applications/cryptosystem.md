---
# === CORE IDENTIFICATION ===
concept: Cryptosystem
slug: cryptosystem

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
pdf_page: 94
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - cipher

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - private-key-cryptography
  - public-key-cryptography
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cryptosystem?"
  - "What are the components of a cryptosystem?"
---

# Quick Definition

A cryptosystem (or cipher) has two parts: encryption, which transforms a plaintext message into ciphertext, and decryption, which reverses this transformation. Cryptosystems are parameterized by keys.

# Core Definition

"A *cryptosystem*, or *cipher*, has two parts: *encryption*, the process of transforming a plaintext message to a ciphertext message, and *decryption*, the reverse transformation of changing a ciphertext message into a plaintext message" (Judson, p. 94). The message to be sent is called the *plaintext*, the disguised version is *ciphertext*, and both are written in an *alphabet* of *letters* or *characters*.

# Prerequisites

This is an introductory concept requiring only basic mathematical background.

# Key Properties

1. Consists of encryption function $f$ and decryption function $f^{-1}$
2. Parameterized by keys that distinguish different instances
3. Two main types: private key (single key) and public key (two keys)
4. The encryption function must be relatively easy to compute
5. The decryption should be difficult without knowledge of the key

# Construction / Recognition

## Components of a Cryptosystem:
1. An alphabet of characters
2. A plaintext message space
3. A ciphertext message space
4. A key space
5. An encryption function $f$ parameterized by the key
6. A decryption function $f^{-1}$

# Context & Application

Cryptography is the study of sending and receiving secret messages. Modern cryptography is heavily dependent on abstract algebra and number theory (Judson, p. 94).

# Examples

**Example 1** (p. 95): Caesar's shift code encodes by $f(p) = p + 3 \bmod 26$, decodes by $f^{-1}(p) = p + 23 \bmod 26$.

# Relationships

## Enables
- **Private Key Cryptography** — Single-key cryptosystems
- **Public Key Cryptography** — Two-key cryptosystems

# Common Errors

- **Error**: Confusing the key with the algorithm
  **Correction**: The algorithm defines the family; the key selects a specific instance

# Common Confusions

- **Confusion**: Thinking encryption and decryption always use the same key
  **Clarification**: Public key cryptosystems use different keys for encryption and decryption

# Source Reference

Chapter 7: Introduction to Cryptography, introductory section, page 94.

# Verification Notes

- Definition source: Direct from p. 94
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
