---
# === CORE IDENTIFICATION ===
concept: Fermat's Little Theorem
slug: fermat-little-theorem

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - euler-theorem
extends:
  - euler-theorem
related:
  - r-n-group
  - euler-phi-function
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Fermat's little theorem?"
  - "How does Lagrange's theorem imply Fermat's little theorem?"
---

# Quick Definition

If $p$ is prime and $x$ is not a multiple of $p$, then $x^{p-1} \equiv 1 \pmod{p}$.

# Core Definition

**(11.6) Fermat's Little Theorem.** If $p$ is prime and if $x$ is not a multiple of $p$, then $x^{p-1}$ is congruent to 1 modulo $p$ (Armstrong, p. 66).

**Proof.** Apply Euler's theorem noting that $\varphi(p) = p - 1$.

# Prerequisites

- **Euler's theorem** — Fermat's little theorem is the special case for prime modulus

# Key Properties

1. $x^{p-1} \equiv 1 \pmod{p}$ for all $x$ not divisible by $p$
2. Equivalently, $x^p \equiv x \pmod{p}$ for all integers $x$
3. A special case of Euler's theorem with $\varphi(p) = p - 1$

# Construction / Recognition

## To Apply:
1. Verify $p$ is prime
2. Verify $p$ does not divide $x$
3. Conclude $x^{p-1} \equiv 1 \pmod{p}$

# Context & Application

Armstrong presents Fermat's little theorem as a one-line consequence of Euler's theorem, which itself follows from Lagrange's theorem applied to $R_p$. This demonstrates the power of the group-theoretic approach to number theory.

# Examples

**Example 1**: For $p = 7$, $x = 3$: $3^6 = 729 = 104 \times 7 + 1$, so $3^6 \equiv 1 \pmod{7}$.

# Relationships

## Builds Upon
- **Euler's theorem** — Direct specialisation

## Related
- **$R_n$ group** — $R_p \cong \mathbb{Z}_{p-1}$ when $p$ is prime

# Common Errors

- **Error**: Forgetting the hypothesis that $x$ is not a multiple of $p$
  **Correction**: If $p | x$, then $x^{p-1} \equiv 0 \pmod{p}$, not 1

# Common Confusions

- **Confusion**: Confusing Fermat's little theorem with Fermat's last theorem
  **Clarification**: The little theorem is about modular arithmetic; the last theorem is about the equation $x^n + y^n = z^n$

# Source Reference

Chapter 11: Lagrange's Theorem, Theorem (11.6), p. 66 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (11.6)
- Confidence rationale: HIGH — explicit theorem with proof
- Uncertainties: None
