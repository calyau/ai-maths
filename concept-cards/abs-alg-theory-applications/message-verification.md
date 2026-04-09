---
# === CORE IDENTIFICATION ===
concept: Message Verification
slug: message-verification

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
pdf_page: 98
section: "Message Verification"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - digital signature

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rsa-cryptosystem
extends: []
related:
  - public-key-cryptography
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can you verify who sent an RSA-encrypted message?"
  - "What is message verification in public key cryptography?"
---

# Quick Definition

Message verification in RSA allows the sender to prove authenticity by first "decrypting" the message with their private key, then encrypting with the recipient's public key. Only the true sender could have created the signature.

# Core Definition

To verify a message, Bob (sender) first computes $x' = x^{D'} \bmod n'$ using his own private key, then encrypts with Alice's public key: $y' = x'^E \bmod n$. Alice decodes with her private key, then verifies using Bob's public key. "Only Bob has the ability to form $x'$" (Judson, p. 98), ensuring authenticity.

# Prerequisites

- **RSA Cryptosystem** — Verification uses RSA encryption and decryption

# Key Properties

1. Anyone can encrypt, but only the key holder can "sign" (decrypt with private key)
2. The signature can be verified by anyone with the sender's public key
3. Provides both confidentiality and authenticity
4. The process: sign with sender's private key, encrypt with recipient's public key

# Construction / Recognition

## To Send a Verified Message (Bob to Alice):
1. Bob signs: $x' = x^{D'} \bmod n'$ (using Bob's private key)
2. Bob encrypts: $y' = x'^E \bmod n$ (using Alice's public key)
3. Alice decrypts: $x' = y'^D \bmod n$ (using Alice's private key)
4. Alice verifies: $x = x'^{E'} \bmod n'$ (using Bob's public key)

# Context & Application

Message verification solves the authentication problem in public key systems. Since anyone can send an encrypted message to Alice, she needs a way to confirm the sender's identity.

# Examples

**Example 1** (p. 98): Bob has keys $(n', E')$ public and $(n', D')$ private. Alice has keys $(n, E)$ public and $(n, D)$ private. Bob creates $x' = x^{D'} \bmod n'$, then sends $y' = x'^E \bmod n$.

# Relationships

## Builds Upon
- **RSA Cryptosystem** — Uses RSA for both signing and encryption

## Related
- **Public Key Cryptography** — Verification is a feature of public key systems

# Common Errors

- **Error**: Encrypting first then signing (wrong order)
  **Correction**: Sign first (with sender's private key), then encrypt (with recipient's public key)

# Common Confusions

- **Confusion**: Thinking encryption alone provides authentication
  **Clarification**: Encryption provides confidentiality; verification (signing) provides authentication

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.2, "Message Verification," page 98.

# Verification Notes

- Definition source: Direct from p. 98
- Confidence rationale: Explicit procedure described
- Uncertainties: None
- Cross-reference status: Verified
