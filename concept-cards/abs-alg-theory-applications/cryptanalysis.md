---
concept: Cryptanalysis
slug: cryptanalysis
category: applications-crypto
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Introduction to Cryptography"
chapter_number: 7
pdf_page: 95
section: "7.1 Private Key Cryptography"
extraction_confidence: high
aliases:
  - frequency analysis
prerequisites:
  - cryptosystem
extends: []
related:
  - monoalphabetic-cryptosystem
  - private-key-cryptography
contrasts_with: []
answers_questions:
  - "What is cryptanalysis?"
  - "How is frequency analysis used to break ciphers?"
---

# Quick Definition

Cryptanalysis is the study of deciphering intercepted messages without knowledge of the key. Frequency analysis, which exploits the statistical properties of natural language, is a primary tool for breaking monoalphabetic ciphers.

# Core Definition

"*Cryptanalysis* is concerned with deciphering a received or intercepted message. Methods from probability and statistics are great aids in deciphering an intercepted message; for example, the frequency analysis of the characters appearing in the intercepted message often makes its decryption possible" (Judson, p. 95).

# Prerequisites

- **Cryptosystem** — Cryptanalysis attempts to break cryptosystems

# Key Properties

1. Uses statistical properties of natural language (letter frequencies)
2. The letter E (= 04) is the most common in English
3. Effective against monoalphabetic ciphers
4. Less effective against polyalphabetic ciphers
5. Can be extended to digram (pair) frequency analysis

# Construction / Recognition

## To Perform Frequency Analysis:
1. Count the frequency of each character in the ciphertext
2. Match the most frequent ciphertext character to E (or other common letters)
3. Deduce the key from this correspondence
4. Verify by decrypting and checking for sensible plaintext

# Context & Application

Frequency analysis was developed by Arab scholars in the 1400s. It renders monoalphabetic ciphers insecure and motivates the development of more sophisticated encryption methods.

# Examples

**Example 1** (p. 95-96): If S (= 18) is the most frequent ciphertext letter, then $18 = 4 + b \bmod 26$ gives $b = 14$. The encryption function is $f(p) = p + 14 \bmod 26$.

# Relationships

## Builds Upon
- **Cryptosystem** — Cryptanalysis targets cryptosystems

## Related
- **Monoalphabetic Cryptosystem** — Most vulnerable to frequency analysis

# Common Errors

- **Error**: Assuming the most frequent letter always corresponds to E
  **Correction**: This is a heuristic; short messages may not follow standard frequency distributions

# Common Confusions

- **Confusion**: Thinking frequency analysis only works on shift ciphers
  **Clarification**: It works on any monoalphabetic cipher; for polyalphabetic, frequency analysis on pairs/blocks can still be applied

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.1, Example 7.2, pages 95-96.

# Verification Notes

- Definition source: Direct from p. 95
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
