---
# === CORE IDENTIFICATION ===
concept: Public Key Cryptography
slug: public-key-cryptography

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
section: "7.2 Public Key Cryptography"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - asymmetric cryptography

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cryptosystem
extends: []
related:
  - rsa-cryptosystem
  - message-verification
contrasts_with:
  - private-key-cryptography

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is public key cryptography?"
  - "How does public key cryptography differ from private key?"
---

# Quick Definition

Public key cryptography uses two separate keys: a public encoding key (known to everyone) and a private decoding key (known only to the recipient). Knowledge of the encoding key does not reveal the decoding key.

# Core Definition

"Systems that use two separate keys, one for encoding and another for decoding, are called *public key cryptosystems*. Since knowledge of the encoding key does not allow anyone to guess at the decoding key, the encoding key can be made public" (Judson, p. 94). Proposed by Diffie and Hellman in 1976, it "removes the requirement that the encoding key be kept secret" (p. 97).

# Prerequisites

- **Cryptosystem** — Public key is a type of cryptosystem

# Key Properties

1. Separate encryption (public) and decryption (private) keys
2. The encryption function $f$ is easy to compute
3. $f^{-1}$ is computationally infeasible without the private key
4. Anyone can encrypt messages to a recipient
5. Only the recipient (who holds the private key) can decrypt
6. No system has been provably shown to be "one-way" (p. 97)

# Construction / Recognition

## To Use:
1. Recipient generates a public/private key pair
2. Recipient publishes the public key
3. Sender encrypts using the public key
4. Recipient decrypts using the private key

# Context & Application

Public key cryptography solved the key distribution problem of private key systems. The concept was revolutionary because it decoupled the ability to encrypt from the ability to decrypt, enabling secure communication without prior shared secrets.

# Examples

**Example 1** (p. 94): Alice and Bob can both send encrypted messages to Charlie using Charlie's public encoding key. Only Charlie knows the decoding key.

# Relationships

## Builds Upon
- **Cryptosystem** — A type of cryptosystem

## Enables
- **RSA Cryptosystem** — The most prominent public key system
- **Message Verification** — Public key enables digital signatures

## Contrasts With
- **Private Key Cryptography** — Uses a single shared key

# Common Errors

- **Error**: Assuming the public key can be used for decryption
  **Correction**: The public key is only for encryption; decryption requires the private key

# Common Confusions

- **Confusion**: Thinking public key cryptography has been proven secure
  **Clarification**: "No system has been proposed that has been proven to be 'one-way'" (p. 97)

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.2, pages 96-98.

# Verification Notes

- Definition source: Direct from pp. 94, 96-97
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
