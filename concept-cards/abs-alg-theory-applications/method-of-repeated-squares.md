---
# === CORE IDENTIFICATION ===
concept: Method of Repeated Squares
slug: method-of-repeated-squares

# === CLASSIFICATION ===
category: cyclic-groups
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Cyclic Groups"
chapter_number: 4
pdf_page: 66
section: "The Method of Repeated Squares"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - fast exponentiation
  - binary exponentiation
  - repeated squaring

# === TYPED RELATIONSHIPS ===
prerequisites:
  - modular-arithmetic
  - laws-of-exponents-groups
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a cyclic group?"
---

# Quick Definition

The method of repeated squares is an efficient algorithm for computing large powers $a^n \pmod{m}$ by expressing $n$ in binary and using successive squaring, reducing the number of multiplications from $n$ to about $\log_2 n$.

# Core Definition

The method works by writing the exponent $a$ in binary: $a = 2^{k_1} + 2^{k_2} + \cdots + 2^{k_n}$, then computing $b^a \pmod{n}$ as $b^{2^{k_1}} \cdot b^{2^{k_2}} \cdots b^{2^{k_n}} \pmod{n}$. Each $b^{2^k}$ is computed by repeatedly squaring (Judson, pp. 66-68).

# Prerequisites

- **Modular arithmetic** — Computations are performed modulo $n$
- **Laws of exponents in groups** — $b^{x+y} = b^x \cdot b^y$

# Key Properties

1. Reduces exponentiation from $O(n)$ to $O(\log n)$ multiplications
2. Based on binary representation of the exponent
3. Each step involves squaring the previous result and reducing mod $n$
4. Essential for practical RSA cryptography

# Construction / Recognition

## To Compute $b^a \pmod{n}$:
1. Write $a$ in binary: $a = 2^{k_1} + 2^{k_2} + \cdots$
2. Compute $b^{2^0} \pmod{n}$, $b^{2^1} \pmod{n}$, ..., $b^{2^k} \pmod{n}$ by repeated squaring
3. Multiply together the terms $b^{2^{k_i}} \pmod{n}$ for each 1-bit in the binary representation
4. Reduce modulo $n$ at each step

# Context & Application

The method of repeated squares is essential for RSA cryptography (Chapter 7), where one must compute large powers modulo $n$ efficiently. Without this method, encryption and decryption would be computationally infeasible.

# Examples

**Example 1** (pp. 67-68): Compute $271^{321} \pmod{481}$. Since $321 = 2^0 + 2^6 + 2^8$:
- $271^{2^1} \equiv 329 \pmod{481}$
- $271^{2^2} \equiv 16 \pmod{481}$
- Continuing: $271^{2^6} \equiv 419 \pmod{481}$, $271^{2^8} \equiv 16 \pmod{481}$
- Result: $271^{321} \equiv 271 \cdot 419 \cdot 16 \equiv 47 \pmod{481}$

# Relationships

## Builds Upon
- **modular-arithmetic** — Operations performed mod $n$
- **laws-of-exponents-groups** — $b^{x+y} = b^x b^y$

# Common Errors

- **Error**: Forgetting to reduce modulo $n$ at each squaring step
  **Correction**: Always reduce mod $n$ after each multiplication to keep numbers manageable

# Common Confusions

- **Confusion**: Thinking you need to compute $b^a$ first and then reduce mod $n$
  **Clarification**: Reducing at each step is equivalent and keeps intermediate values small

# Source Reference

Chapter 4: Cyclic Groups, Section 4.3, pages 66-68.

# Verification Notes

- Definition source: Synthesized from Section 4.3
- Confidence: HIGH — explicit algorithm with worked example
- Cross-reference status: Verified
- Uncertainties: None
