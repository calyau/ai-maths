---
# === CORE IDENTIFICATION ===
concept: Euler's Theorem
slug: euler-theorem

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Lagrange's Theorem"
chapter_number: 11
pdf_page: 64
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Euler's totient theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - element-power-equals-identity
  - r-n-group
  - euler-phi-function
extends:
  - lagrange-theorem
related:
  - fermat-little-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Euler's theorem in number theory?"
  - "How does Lagrange's theorem yield results in number theory?"
---

# Quick Definition

If the highest common factor of $x$ and $n$ is 1, then $x^{\varphi(n)} \equiv 1 \pmod{n}$.

# Core Definition

**(11.5) Euler's Theorem.** If the highest common factor of $x$ and $n$ is 1, then $x^{\varphi(n)}$ is congruent to 1 modulo $n$ (Armstrong, p. 66).

**Proof.** Divide $x$ by $n$ to give a remainder $m$ which belongs to $R_n$. By Corollary (11.4), $m^{\varphi(n)} \equiv 1 \pmod{n}$. Since $x^{\varphi(n)} \equiv m^{\varphi(n)} \pmod{n}$, the result follows.

# Prerequisites

- **$x^{|G|} = e$** — The group-theoretic result applied to $R_n$
- **$R_n$ group** — The multiplicative group modulo $n$
- **Euler's phi-function** — The order of $R_n$

# Key Properties

1. Holds for all integers $x$ coprime to $n$
2. The exponent $\varphi(n)$ is optimal in the sense that it equals $|R_n|$
3. Specialises to Fermat's little theorem when $n$ is prime

# Construction / Recognition

## To Apply:
1. Verify $\gcd(x, n) = 1$
2. Compute $\varphi(n)$
3. Conclude $x^{\varphi(n)} \equiv 1 \pmod{n}$

# Context & Application

Armstrong derives Euler's theorem as a direct application of Lagrange's theorem to the group $R_n$, demonstrating the power of abstract algebra to yield concrete number-theoretic results.

# Examples

**Example 1**: Since $\varphi(9) = 6$, any integer coprime to 9 satisfies $x^6 \equiv 1 \pmod{9}$. For instance, $2^6 = 64 \equiv 1 \pmod{9}$.

# Relationships

## Builds Upon
- **Lagrange's theorem** — Via Corollary (11.4) applied to $R_n$
- **$R_n$ group** — The group in which the theorem is proved

## Enables
- **Fermat's little theorem** — Special case for primes

# Common Errors

- **Error**: Applying the theorem when $\gcd(x, n) \neq 1$
  **Correction**: The hypothesis $\gcd(x, n) = 1$ is essential; for example, $2^{\varphi(4)} = 2^2 = 4 \not\equiv 1 \pmod{4}$

# Common Confusions

- **Confusion**: Thinking this is a purely number-theoretic result
  **Clarification**: Armstrong presents it as a corollary of Lagrange's theorem, showing the algebraic underpinning of a classical number theory result

# Source Reference

Chapter 11: Lagrange's Theorem, Theorem (11.5), p. 66 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (11.5)
- Confidence rationale: HIGH — explicit theorem with proof
- Uncertainties: None
