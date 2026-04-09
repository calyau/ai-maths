---
# === CORE IDENTIFICATION ===
concept: Every PID is a UFD
slug: pid-implies-ufd

# === CLASSIFICATION ===
category: domain-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Integral Domains"
chapter_number: 18
pdf_page: 244
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - principal-ideal-domain
  - unique-factorization-domain
  - ascending-chain-condition
extends: []
related:
  - domain-hierarchy
  - irreducible-element
  - prime-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why is every PID a UFD?"
  - "What distinguishes a PID from a UFD?"
---

# Quick Definition

Every principal ideal domain is a unique factorization domain. The proof uses the ACC to guarantee existence of factorizations and the fact that irreducible = prime in PIDs to guarantee uniqueness.

# Core Definition

"Every PID is a UFD" (Judson, Theorem 18.15, p. 244). The proof has two parts: (1) the ACC in PIDs (Lemma 18.14) ensures that factorization into irreducibles exists; (2) the fact that irreducible implies prime in PIDs (Corollary 18.13) ensures uniqueness.

# Prerequisites

- **PID** — The hypothesis
- **UFD** — The conclusion
- **ACC** — Used to show existence of factorization

# Key Properties

1. ACC ensures factorization terminates (existence)
2. Irreducible $\Rightarrow$ prime in PIDs (Corollary 18.13) ensures uniqueness
3. The converse fails: $\mathbb{Z}[x]$ is a UFD but not a PID

# Construction / Recognition

## Proof Outline:
1. Use ACC to show every nonzero non-unit factors into irreducibles
2. Use "irreducible = prime" to show the factorization is unique up to associates

# Context & Application

This theorem is the key link in the chain Euclidean domain $\to$ PID $\to$ UFD. It shows that the ideal-theoretic property (every ideal principal) has deep consequences for factorization.

# Examples

**Example 1**: $\mathbb{Z}$ is a PID, hence a UFD (which is the Fundamental Theorem of Arithmetic).

**Example 2**: $F[x]$ is a PID, hence a UFD.

**Example 3** (p. 245): $\mathbb{Z}[x]$ is a UFD but NOT a PID, showing the converse fails.

# Relationships

## Builds Upon
- **PID** — The starting assumption
- **ACC** — Ensures factorization exists

## Enables
- **Domain hierarchy** — Establishes PID $\subset$ UFD

# Common Errors

- **Error**: Assuming the converse (UFD $\Rightarrow$ PID)
  **Correction**: $\mathbb{Z}[x]$ is a counterexample

# Common Confusions

- **Confusion**: Thinking the proof is trivial
  **Clarification**: Both existence and uniqueness require nontrivial arguments; existence uses ACC, uniqueness uses prime = irreducible

# Source Reference

Chapter 18: Integral Domains, Section 18.2, Theorem 18.15, pages 244-245.

# Verification Notes

- Definition source: Direct from Theorem 18.15
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
