---
# === CORE IDENTIFICATION ===
concept: Proof by Contradiction
slug: proof-by-contradiction

# === CLASSIFICATION ===
category: foundations
subcategory: logic-and-proofs
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 15
section: "A Short Note on Proofs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - indirect proof
  - reductio ad absurdum

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mathematical-proof
extends: []
related:
  - contrapositive
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

Proof by contradiction assumes the negation of what you want to prove, then derives a logical contradiction, thereby establishing the original statement.

# Core Definition

"Although it is usually better to find a direct proof of a theorem, this task can sometimes be difficult. It may be easier to assume that the theorem that you are trying to prove is false, and to hope that in the course of your argument you are forced to make some statement that cannot possibly be true" (Judson, p. 15).

# Prerequisites

- **Mathematical proof** — Contradiction is a proof technique

# Key Properties

1. Assume the negation of the desired conclusion
2. Derive a statement that contradicts a known truth
3. Conclude the original statement must be true
4. Works because a true hypothesis cannot lead to a contradiction

# Context & Application

Proof by contradiction is used for several important results in this text, including Euclid's proof of infinitely many primes (Theorem 2.14) and the existence part of the Fundamental Theorem of Arithmetic.

# Examples

**Example 1** (p. 35): Euclid's proof of infinitely many primes: assume only finitely many primes $p_1, \ldots, p_n$. Then $P = p_1 p_2 \cdots p_n + 1$ is not divisible by any $p_i$ (since division leaves remainder 1), contradicting the assumption that $p_1, \ldots, p_n$ are all primes.

# Relationships

## Builds Upon
- **mathematical-proof** — A proof technique

## Related
- **contrapositive** — Another indirect proof method

# Common Errors

- **Error**: Deriving a "weird" result and claiming contradiction without actual logical inconsistency
  **Correction**: A genuine contradiction must directly contradict a known fact or assumption

# Source Reference

Chapter 1: Preliminaries, Section 1.1, page 15.

# Verification Notes

- Definition source: Direct from p. 15
- Confidence: HIGH — explicit description
- Cross-reference status: Verified
- Uncertainties: None
