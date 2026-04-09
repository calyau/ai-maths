---
# === CORE IDENTIFICATION ===
concept: RSA Cryptosystem
slug: rsa-cryptosystem

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
pdf_page: 97
section: "The RSA Cryptosystem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - RSA
  - Rivest-Shamir-Adleman cryptosystem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - public-key-cryptography
  - eulers-theorem
  - euler-phi-function
extends: []
related:
  - fermats-little-theorem
  - message-verification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I encrypt/decrypt using RSA?"
  - "What is the RSA cryptosystem?"
  - "Why does RSA decryption work?"
---

# Quick Definition

The RSA cryptosystem is a public key system based on the difficulty of factoring large numbers. Encryption uses $y = x^E \bmod n$; decryption uses $x = y^D \bmod n$, where $n = pq$ for large primes $p, q$.

# Core Definition

The RSA cryptosystem (Rivest, Shamir, Adleman, 1978) works as follows: choose two large primes $p$ and $q$, compute $n = pq$ and $m = \phi(n) = (p-1)(q-1)$. Choose $E$ with $\gcd(E, m) = 1$ and find $D$ such that $DE \equiv 1 \pmod{m}$. Public key: $(n, E)$. Private key: $(n, D)$. Encryption: $y = x^E \bmod n$. Decryption: $x = y^D \bmod n$ (Judson, pp. 97-98).

# Prerequisites

- **Public Key Cryptography** — RSA is a public key system
- **Euler's Theorem** — Correctness proof: $y^D = x^{DE} = x^{k\phi(n)+1} = x \bmod n$
- **Euler Phi-Function** — Key generation uses $\phi(n) = (p-1)(q-1)$

# Key Properties

1. Security relies on the difficulty of factoring $n = pq$
2. Public key $(n, E)$ can be published; private key $D$ is secret
3. Correctness: $y^D \equiv (x^E)^D = x^{DE} = x^{k\phi(n)+1} \equiv x \pmod{n}$ (by Euler's Theorem)
4. Key generation requires finding large primes and computing modular inverse
5. Breaking RSA requires factoring $n$, which is computationally infeasible for large $n$

# Construction / Recognition

## Key Generation:
1. Choose two large primes $p$ and $q$
2. Compute $n = pq$
3. Compute $\phi(n) = (p-1)(q-1)$
4. Choose $E$ with $\gcd(E, \phi(n)) = 1$
5. Compute $D$ such that $DE \equiv 1 \pmod{\phi(n)}$ (using Euclidean algorithm)
6. Public key: $(n, E)$; Private key: $(n, D)$

## To Encrypt:
1. Digitize message into blocks $x < n$
2. Compute $y = x^E \bmod n$

## To Decrypt:
1. Compute $x = y^D \bmod n$

# Context & Application

RSA is the most widely used public key cryptosystem. Its security depends on the computational difficulty of factoring products of two large primes. The correctness proof elegantly applies Euler's Theorem from group theory to number-theoretic encryption.

# Examples

**Example 1** (p. 97): Let $p = 23$, $q = 29$. Then $n = 667$, $\phi(n) = 616$. Choose $E = 487$ (since $\gcd(616, 487) = 1$). Compute: $25^{487} \bmod 667 = 169$. Find $D = 191$ (since $191 \cdot 487 \equiv 1 \pmod{616}$). Verify: $169^{191} \bmod 667 = 25$.

# Relationships

## Builds Upon
- **Public Key Cryptography** — RSA is a public key system
- **Euler's Theorem** — Guarantees correctness of decryption
- **Euler Phi-Function** — Used in key generation

## Enables
- **Message Verification** — RSA supports digital signatures

## Related
- **Fermat's Little Theorem** — Special case used in the proof

# Common Errors

- **Error**: Choosing $E$ that is not coprime to $\phi(n)$
  **Correction**: Must have $\gcd(E, \phi(n)) = 1$ for $D$ to exist

- **Error**: Using primes $p$ and $q$ that are too small or too close together
  **Correction**: Primes should be large (150+ digits) and of different magnitudes

# Common Confusions

- **Confusion**: Thinking RSA has been proven secure
  **Clarification**: It has never been proven that factoring is computationally hard; RSA's security is empirical

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.2, "The RSA Cryptosystem," Example 7.5, pages 97-98.

# Verification Notes

- Definition source: Direct from pp. 97-98
- Confidence rationale: Detailed algorithm with worked example
- Uncertainties: None
- Cross-reference status: Verified
