---
# === CORE IDENTIFICATION ===
concept: Euler's Theorem
slug: eulers-theorem

# === CLASSIFICATION ===
category: group-structure
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cosets and Lagrange's Theorem"
chapter_number: 6
pdf_page: 90
section: "6.3 Fermat's and Euler's Theorems"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - euler-phi-function
  - lagranges-theorem
extends: []
related:
  - fermats-little-theorem
  - rsa-cryptosystem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Euler's theorem?"
  - "How does Lagrange's theorem imply Euler's theorem?"
---

# Quick Definition

Euler's Theorem states that if $a$ and $n$ are integers with $n > 0$ and $\gcd(a, n) = 1$, then $a^{\phi(n)} \equiv 1 \pmod{n}$.

# Core Definition

**Theorem 6.18 (Euler's Theorem):** "Let $a$ and $n$ be integers such that $n > 0$ and $\gcd(a, n) = 1$. Then $a^{\phi(n)} \equiv 1 \pmod{n}$" (Judson, p. 90). The proof follows from Lagrange's Theorem applied to $U(n)$: since $|U(n)| = \phi(n)$, we have $a^{\phi(n)} = 1$ for all $a \in U(n)$.

# Prerequisites

- **Euler Phi-Function** — The exponent is $\phi(n)$
- **Lagrange's Theorem** — The order of any element divides the group order

# Key Properties

1. Requires $\gcd(a, n) = 1$
2. Generalizes Fermat's Little Theorem (which is the special case $n = p$ prime)
3. Follows directly from Lagrange's Theorem applied to $U(n)$
4. Provides the theoretical basis for RSA decryption

# Construction / Recognition

## To Apply:
1. Verify $\gcd(a, n) = 1$
2. Compute $\phi(n)$
3. Conclude $a^{\phi(n)} \equiv 1 \pmod{n}$

# Context & Application

Euler's Theorem is a bridge between group theory and number theory. It is essential for the RSA cryptosystem, where the decryption works because $x^{DE} = x^{k\phi(n)+1} = (x^{\phi(n)})^k \cdot x \equiv x \pmod{n}$.

# Examples

**Example 1** (p. 90): $|U(12)| = \phi(12) = 4$, so for any $a$ with $\gcd(a, 12) = 1$, we have $a^4 \equiv 1 \pmod{12}$. For instance, $5^4 = 625 \equiv 1 \pmod{12}$.

# Relationships

## Builds Upon
- **Euler Phi-Function** — $\phi(n)$ is the exponent
- **Lagrange's Theorem** — Euler's Theorem is a corollary

## Enables
- **RSA Cryptosystem** — Decryption relies on Euler's Theorem

## Related
- **Fermat's Little Theorem** — Special case for prime modulus

# Common Errors

- **Error**: Applying Euler's Theorem when $\gcd(a, n) \neq 1$
  **Correction**: The theorem requires $a$ and $n$ to be coprime

# Common Confusions

- **Confusion**: Thinking Euler's Theorem gives the *order* of $a$ modulo $n$
  **Clarification**: $\phi(n)$ is a *multiple* of the order of $a$, not necessarily the order itself

# Source Reference

Chapter 6: Cosets and Lagrange's Theorem, Section 6.3, Theorem 6.18, page 90.

# Verification Notes

- Definition source: Direct from Theorem 6.18
- Confidence rationale: Explicit named theorem
- Uncertainties: None
- Cross-reference status: Verified
