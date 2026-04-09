---
concept: Plaintext and Ciphertext
slug: plaintext-and-ciphertext
category: applications-crypto
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Introduction to Cryptography"
chapter_number: 7
pdf_page: 94
section: null
extraction_confidence: high
aliases: []
prerequisites: []
extends: []
related:
  - cryptosystem
  - private-key-cryptography
contrasts_with: []
answers_questions:
  - "What are plaintext and ciphertext?"
---

# Quick Definition

The plaintext is the original unencrypted message. The ciphertext is the encrypted (disguised) version. Both are written in an alphabet of characters that may include letters, digits, and punctuation.

# Core Definition

"The message to be sent is called the *plaintext* message. The disguised message is called the *ciphertext*. The plaintext and the ciphertext are both written in an *alphabet*, consisting of *letters* or *characters*" (Judson, p. 94).

# Prerequisites

No prerequisites; this is introductory terminology.

# Key Properties

1. Plaintext is the original message before encryption
2. Ciphertext is the message after encryption
3. Both are composed of characters from an alphabet
4. Characters can include letters, digits, punctuation, and blanks
5. Encryption transforms plaintext to ciphertext; decryption reverses

# Construction / Recognition

## Standard Digitization:
1. Map A = 00, B = 01, ..., Z = 25 (26-letter alphabet)
2. Encryption function maps plaintext digits to ciphertext digits

# Context & Application

These are the fundamental terms of cryptography. The goal is to transmit plaintext as ciphertext so that only the intended recipient can recover the original plaintext.

# Examples

**Example 1** (p. 95): The plaintext "ALGEBRA" is digitized as 0, 11, 6, 4, 1, 17, 0. After encryption with $f(p) = p + 3 \bmod 26$, the ciphertext is "DOJHEUD" (3, 14, 9, 7, 4, 20, 3).

# Relationships

## Enables
- **Cryptosystem** — Defined in terms of plaintext and ciphertext transformations

# Common Errors

- **Error**: Confusing which is plaintext and which is ciphertext
  **Correction**: Plaintext is the readable original; ciphertext is the encoded version

# Common Confusions

- **Confusion**: Thinking plaintext must be in English
  **Clarification**: Plaintext can be any data in any alphabet, including binary

# Source Reference

Chapter 7: Introduction to Cryptography, introductory section, page 94.

# Verification Notes

- Definition source: Direct from p. 94
- Confidence rationale: Explicit definitions
- Uncertainties: None
- Cross-reference status: Verified
