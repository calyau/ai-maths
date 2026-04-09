---
# === CORE IDENTIFICATION ===
concept: Pseudoprime
slug: pseudoprime

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
pdf_page: 102
section: "7.5 Additional Exercises: Primality and Factoring"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Fermat pseudoprime
  - pseudoprime base 2

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fermats-little-theorem
extends: []
related:
  - carmichael-number
  - rsa-cryptosystem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a pseudoprime?"
  - "Why can't Fermat's Little Theorem alone test primality?"
---

# Quick Definition

A pseudoprime is an odd composite number $n$ satisfying $2^{n-1} \equiv 1 \pmod{n}$. It "passes" the Fermat primality test despite being composite, showing the test is necessary but not sufficient.

# Core Definition

"We say that an odd composite number $n$ is a *pseudoprime* if $2^{n-1} \equiv 1 \pmod{n}$" (Judson, p. 102). More generally, $n$ is a *pseudoprime base $b$* if $b^{n-1} \equiv 1 \pmod{n}$ with $\gcd(b, n) = 1$.

# Prerequisites

- **Fermat's Little Theorem** — Pseudoprimes are composites that satisfy Fermat's condition

# Key Properties

1. A pseudoprime passes the Fermat test but is not prime
2. Pseudoprimes are relatively rare among odd numbers
3. 341 is a pseudoprime base 2 but not base 3
4. A number can be a pseudoprime to some bases but not others

# Construction / Recognition

## To Test:
1. Compute $2^{n-1} \bmod n$
2. If the result is not 1, $n$ is definitely composite
3. If the result is 1, $n$ is either prime or a pseudoprime

# Context & Application

Pseudoprimes are important in computational number theory and cryptography because they show the limitations of the Fermat primality test. More sophisticated tests (Miller-Rabin) are needed for reliable primality testing.

# Examples

**Example 1** (p. 102): $2^{14} \equiv 4 \pmod{15}$, so 15 is not a pseudoprime. But $2^{16} \equiv 1 \pmod{17}$, consistent with 17 being prime.

**Example 2** (p. 102): 341 is a pseudoprime base 2 ($2^{340} \equiv 1 \pmod{341}$) but 341 = 11 $\times$ 31 is composite.

# Relationships

## Builds Upon
- **Fermat's Little Theorem** — Defines the test that pseudoprimes "pass"

## Related
- **Carmichael Number** — Composite numbers that are pseudoprime to all coprime bases
- **RSA Cryptosystem** — Primality testing is needed for key generation

# Common Errors

- **Error**: Declaring a number prime because it passes the Fermat test
  **Correction**: The Fermat test is necessary but not sufficient; pseudoprimes exist

# Common Confusions

- **Confusion**: Thinking pseudoprimes are common
  **Clarification**: Pseudoprimes are very rare; the Fermat test is a good heuristic but not definitive

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.5, page 102.

# Verification Notes

- Definition source: Direct from p. 102
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
