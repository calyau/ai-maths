---
concept: Carmichael Number
slug: carmichael-number
category: applications-crypto
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Introduction to Cryptography"
chapter_number: 7
pdf_page: 102
section: "7.5 Additional Exercises: Primality and Factoring"
extraction_confidence: high
aliases: []
prerequisites:
  - pseudoprime
extends:
  - pseudoprime
related:
  - fermats-little-theorem
  - rsa-cryptosystem
contrasts_with: []
answers_questions:
  - "What is a Carmichael number?"
---

# Quick Definition

A Carmichael number is a composite number that is a pseudoprime to all bases relatively prime to it. The smallest is 561 = 3 $\cdot$ 11 $\cdot$ 17. There are infinitely many Carmichael numbers, though they are very rare.

# Core Definition

"There exist composite numbers that are pseudoprimes for all bases to which they are relatively prime. These numbers are called *Carmichael numbers*" (Judson, p. 102). The first Carmichael number is 561 = 3 $\cdot$ 11 $\cdot$ 17. In 1992, Alford, Granville, and Pomerance proved there are infinitely many.

# Prerequisites

- **Pseudoprime** — Carmichael numbers are pseudoprimes to all coprime bases

# Key Properties

1. Composite number $n$ with $b^{n-1} \equiv 1 \pmod{n}$ for all $b$ with $\gcd(b, n) = 1$
2. The smallest is 561 = 3 $\cdot$ 11 $\cdot$ 17
3. There are infinitely many (proved 1992)
4. Very rare: only 2163 below $25 \times 10^9$
5. Cannot be detected by the Fermat test alone

# Construction / Recognition

## To Test:
1. Factor $n$ (if possible)
2. Check if $n$ is composite
3. Verify $b^{n-1} \equiv 1 \pmod{n}$ for all $b$ coprime to $n$

# Context & Application

Carmichael numbers show that the Fermat primality test has inherent limitations. More sophisticated tests (Miller-Rabin) are needed for reliable primality testing in cryptographic applications.

# Examples

**Example 1** (p. 102): 561 = 3 $\cdot$ 11 $\cdot$ 17 is the first Carmichael number.

# Relationships

## Builds Upon
- **Pseudoprime** — Carmichael numbers are universal pseudoprimes

## Related
- **Fermat's Little Theorem** — Carmichael numbers satisfy the Fermat condition for all coprime bases
- **RSA Cryptosystem** — Motivates the need for better primality tests

# Common Errors

- **Error**: Relying on the Fermat test with a single base
  **Correction**: Use multiple bases, or better, use Miller-Rabin which can detect Carmichael numbers

# Common Confusions

- **Confusion**: Thinking Carmichael numbers are common
  **Clarification**: They are exceedingly rare (only 2163 below $2.5 \times 10^{10}$)

# Source Reference

Chapter 7: Introduction to Cryptography, Section 7.5, page 102.

# Verification Notes

- Definition source: Direct from p. 102
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
