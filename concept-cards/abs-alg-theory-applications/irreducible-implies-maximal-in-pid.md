---
# === CORE IDENTIFICATION ===
concept: Irreducible Implies Maximal Ideal in PID
slug: irreducible-implies-maximal-in-pid

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
pdf_page: 243
section: "18.2 Factorization in Integral Domains"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - principal-ideal-domain
  - irreducible-element
  - maximal-ideal
extends: []
related:
  - prime-element
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When does an irreducible element generate a maximal ideal?"
  - "Are irreducible and prime the same in a PID?"
---

# Quick Definition

In a PID, $\langle p \rangle$ is a maximal ideal if and only if $p$ is irreducible. Consequently, in a PID, every irreducible element is prime.

# Core Definition

"Let $D$ be a PID and $\langle p \rangle$ be a nonzero ideal in $D$. Then $\langle p \rangle$ is a maximal ideal if and only if $p$ is irreducible" (Judson, Theorem 18.12, p. 243). As a corollary, "Let $D$ be a PID. If $p$ is irreducible, then $p$ is prime" (Corollary 18.13, p. 243).

# Prerequisites

- **PID** — The result requires a PID
- **Irreducible element** — The element $p$ must be irreducible
- **Maximal ideal** — The conclusion involves maximal ideals

# Key Properties

1. In a PID: irreducible $\Leftrightarrow \langle p \rangle$ maximal
2. Maximal $\Rightarrow$ prime (Corollary 16.40), so irreducible $\Rightarrow$ prime in PIDs
3. This equivalence fails in non-PIDs

# Construction / Recognition

## To Apply:
1. Verify $D$ is a PID
2. Test if $p$ is irreducible
3. Conclude $\langle p \rangle$ is maximal and $p$ is prime

# Context & Application

This theorem connects element-level properties (irreducibility) to ideal-level properties (maximality) in PIDs. It is a key step in proving every PID is a UFD.

# Examples

**Example 1**: In $\mathbb{Z}$ (a PID), $\langle 5 \rangle = 5\mathbb{Z}$ is maximal since $5$ is irreducible (prime).

**Example 2**: In $\mathbb{Z}[x]$ (not a PID), $\langle x \rangle$ is prime but not maximal.

# Relationships

## Builds Upon
- **PID** — Required hypothesis
- **Irreducible element** — Characterized by maximality of generated ideal

## Enables
- **Irreducible = prime in PID** — Key for unique factorization

# Common Errors

- **Error**: Assuming irreducible implies prime in any integral domain
  **Correction**: This only holds in PIDs; in general domains, irreducible need not be prime

# Common Confusions

- **Confusion**: Thinking this theorem holds in all integral domains
  **Clarification**: The PID hypothesis is essential

# Source Reference

Chapter 18: Integral Domains, Section 18.2, Theorem 18.12 and Corollary 18.13, pages 243-244.

# Verification Notes

- Definition source: Direct from Theorem 18.12 and Corollary 18.13
- Confidence: HIGH — explicit theorems
- Cross-reference status: Verified
- Uncertainties: None
