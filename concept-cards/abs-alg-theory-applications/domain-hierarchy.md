---
# === CORE IDENTIFICATION ===
concept: Domain Hierarchy
slug: domain-hierarchy

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
pdf_page: 248
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "chain of domain types"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - euclidean-domain
  - principal-ideal-domain
  - unique-factorization-domain
  - integral-domain
extends: []
related:
  - field
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Euclidean domains, PIDs, UFDs, and integral domains relate?"
  - "What distinguishes a PID from a UFD?"
---

# Quick Definition

The hierarchy of integral domain types, from most to least structured, is: field $\subset$ Euclidean domain $\subset$ PID $\subset$ UFD $\subset$ integral domain. Each inclusion is strict.

# Core Definition

"Every Euclidean domain is a PID and every PID is a UFD. However, the converse of each of these statements fails" (Judson, Remark 18.33, p. 248). The strict inclusions are:
- Euclidean domain $\subsetneq$ PID: there exist PIDs that are not Euclidean
- PID $\subsetneq$ UFD: $\mathbb{Z}[x]$ is a UFD but not a PID
- UFD $\subsetneq$ integral domain: $\mathbb{Z}[\sqrt{3}i]$ is an integral domain but not a UFD

# Prerequisites

- **Euclidean domain** — Has a division algorithm
- **Principal ideal domain** — Every ideal is principal
- **Unique factorization domain** — Has unique factorization into irreducibles
- **Integral domain** — Commutative ring with identity and no zero divisors

# Key Properties

1. Field $\subset$ Euclidean domain $\subset$ PID $\subset$ UFD $\subset$ integral domain
2. Each inclusion is proper (strict)
3. The proofs use: ED $\to$ PID (Theorem 18.21), PID $\to$ UFD (Theorem 18.15)
4. Counterexamples: $\mathbb{Z}[x]$ (UFD not PID), $\mathbb{Z}[\sqrt{3}i]$ (ID not UFD)

# Construction / Recognition

## To Classify a Domain:
1. Check if it has a Euclidean valuation $\to$ Euclidean domain
2. Check if every ideal is principal $\to$ PID
3. Check if factorization into irreducibles is unique $\to$ UFD
4. If it's a commutative ring with identity and no zero divisors $\to$ integral domain

# Context & Application

This hierarchy organizes the major classes of integral domains by their factorization properties. Understanding where a given domain falls in this hierarchy determines which tools (division algorithm, Euclidean algorithm, unique factorization) are available.

# Examples

**Example 1**: $\mathbb{Z}$ is a Euclidean domain (using absolute value).

**Example 2**: $F[x]$ for a field $F$ is a Euclidean domain (using degree).

**Example 3** (p. 245): $\mathbb{Z}[x]$ is a UFD but not a PID.

**Example 4** (p. 243): $\mathbb{Z}[\sqrt{3}i]$ is an integral domain but not a UFD.

# Relationships

## Related
- **Field** — Every field is a Euclidean domain (trivially)

# Common Errors

- **Error**: Assuming the converses hold (e.g., every UFD is a PID)
  **Correction**: $\mathbb{Z}[x]$ is a UFD but not a PID; the converses are false

# Common Confusions

- **Confusion**: Thinking "integral domain" and "UFD" are the same
  **Clarification**: $\mathbb{Z}[\sqrt{3}i]$ shows that unique factorization can fail in integral domains

# Source Reference

Chapter 18: Integral Domains, Section 18.2, Remark 18.33, page 248.

# Verification Notes

- Definition source: Synthesized from Remark 18.33 and the theorems in Section 18.2
- Confidence: HIGH — explicit remark summarizing the hierarchy
- Cross-reference status: Verified
- Uncertainties: None
