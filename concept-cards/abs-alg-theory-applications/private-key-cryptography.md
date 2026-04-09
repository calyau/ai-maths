---
# === CORE IDENTIFICATION ===
concept: Private Key Cryptography
slug: private-key-cryptography

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
section: "7.1 Private Key Cryptography"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - single key cryptosystem
  - symmetric key cryptography

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cryptosystem
extends: []
related:
  - affine-cryptosystem
  - monoalphabetic-cryptosystem
  - polyalphabetic-cryptosystem
contrasts_with:
  - public-key-cryptography

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is private key cryptography?"
  - "How does a shift cipher work?"
---

# Quick Definition

In private key (symmetric) cryptosystems, the same key is used for both encrypting and decrypting messages. The key must be kept secret and known only to sender and receiver.

# Core Definition

"In *single* or *private key cryptosystems* the same key is used for both encrypting and decrypting messages. To encrypt a plaintext message, we apply to the message some function which is kept secret, say $f$" (Judson, p. 94). The decryption function is $f^{-1}$, which must be easy to compute given the key but difficult to guess from ciphertext alone.

# Prerequisites

- **Cryptosystem** — Private key is a type of cryptosystem

# Key Properties

1. Same key for encryption and decryption
2. The key must be kept secret
3. Separate keys needed for each pair of communicating parties
4. Examples include shift ciphers, affine ciphers, and polyalphabetic ciphers
5. Generally less computationally intensive than public key methods

# Construction / Recognition

## To Use:
1. Sender and receiver agree on a secret key
2. Sender applies encryption function $f$ (parameterized by key) to plaintext
3. Receiver applies $f^{-1}$ (using same key) to recover plaintext

# Context & Application

Private key cryptography dates back to antiquity (Caesar cipher). It is practical for situations where key exchange is feasible but faces the key distribution problem for large networks.

# Examples

**Example 1** (p. 95): Caesar's shift code: $f(p) = p + 3 \bmod 26$. "ALGEBRA" encoded: first digitize to $0, 11, 6, 4, 1, 17, 0$, then shift to get $3, 14, 9, 7, 4, 20, 3$ or "DOJHEUD".

# Relationships

## Builds Upon
- **Cryptosystem** — A type of cryptosystem

## Enables
- **Affine Cryptosystem** — A specific private key scheme
- **Monoalphabetic Cryptosystem** — Simplest private key type
- **Polyalphabetic Cryptosystem** — More secure private key type

## Contrasts With
- **Public Key Cryptography** — Uses separate encoding/decoding keys

# Common Errors

- **Error**: Using the same key for multiple communication pairs in a network
  **Correction**: Each pair needs a separate key to maintain security

# Common Confusions

- **Confusion**: Thinking private key systems are inherently insecure
  **Clarification**: The security depends on key length and algorithm; the challenge is key distribution, not the method itself

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.1, pages 94-97.

# Verification Notes

- Definition source: Direct from p. 94
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
