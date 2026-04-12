---
# === CORE IDENTIFICATION ===
concept: Groups of Prime Order Are Cyclic
slug: groups-of-prime-order-are-cyclic

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
  - lagrange-theorem
  - order-of-element-divides-group-order
extends:
  - lagrange-theorem
related:
  - cyclic-group
  - cauchy-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What can be said about the structure of a group whose order is prime?"
---

# Quick Definition

If a group $G$ has prime order, then $G$ is cyclic. In particular, any non-identity element generates the entire group.

# Core Definition

**(11.3) Corollary.** If $G$ has prime order, then $G$ is cyclic (Armstrong, p. 65).

**Proof.** If $x \in G - \{e\}$, the order of $x$ must equal the order of $G$ by Corollary (11.2), since the only divisors of a prime are 1 and itself, and the order of $x$ is not 1. Therefore $\langle x \rangle = G$.

# Prerequisites

- **Lagrange's theorem** — Provides that element orders divide $|G|$
- **Order of element divides group order** — The immediate prerequisite corollary

# Key Properties

1. If $|G| = p$ (prime), then $G \cong \mathbb{Z}_p$
2. Every non-identity element generates $G$
3. The only subgroups are $\{e\}$ and $G$ itself

# Construction / Recognition

## To Recognize:
1. Compute $|G|$
2. Check if $|G|$ is prime
3. If so, $G$ is cyclic and isomorphic to $\mathbb{Z}_p$

# Context & Application

This corollary completely classifies groups of prime order: there is exactly one group of each prime order (up to isomorphism). Armstrong uses this to classify groups of orders 2, 3, 5, and 7 as cyclic in the enumeration of small groups (Ch. 13, p. 76).

# Examples

**Example 1** (p. 76): Groups of order 2, 3, 5, or 7 are cyclic, being of prime order.

# Relationships

## Builds Upon
- **Lagrange's theorem** — Prime order forces the only element orders to be 1 and $p$
- **Cyclic group** — The result identifies the group as cyclic

## Enables
- **Classification of small groups** — Handles all prime-order cases immediately

# Common Errors

- **Error**: Attempting to use this result for groups of order $p^2$
  **Correction**: Groups of order $p^2$ need not be cyclic (e.g., $\mathbb{Z}_p \times \mathbb{Z}_p$). This result only applies when the order is exactly prime.

# Common Confusions

- **Confusion**: Thinking the result says "cyclic groups have prime order"
  **Clarification**: The converse is false. $\mathbb{Z}_6$ is cyclic but has non-prime order. The result says prime order implies cyclic.

# Source Reference

Chapter 11: Lagrange's Theorem, Corollary (11.3), p. 65 (pdf).

# Verification Notes

- Definition source: Direct from Corollary (11.3)
- Confidence rationale: HIGH — explicit corollary with one-line proof
- Uncertainties: None
