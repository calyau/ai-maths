---
# === CORE IDENTIFICATION ===
concept: Order of Element Divides Group Order
slug: order-of-element-divides-group-order

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
  - cyclic-subgroup
extends:
  - lagrange-theorem
related:
  - groups-of-prime-order-are-cyclic
  - element-power-equals-identity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does Lagrange's theorem say about the order of an element?"
  - "How does an element's order relate to the group's order?"
---

# Quick Definition

In a finite group $G$, the order of every element divides the order of the group.

# Core Definition

**(11.2) Corollary.** The order of every element of $G$ is a divisor of the order of $G$ (Armstrong, p. 65).

**Proof.** The order of an element equals the order of the cyclic subgroup it generates. By Lagrange's theorem, the order of this subgroup divides $|G|$.

# Prerequisites

- **Lagrange's theorem** — This result is a direct corollary
- **Cyclic subgroup** — The order of $x$ equals $|\langle x \rangle|$

# Key Properties

1. If $x \in G$ and $|G| = n$, then the order of $x$ divides $n$
2. Immediately implies $x^{|G|} = e$ for all $x \in G$ (Corollary 11.4)
3. Constrains which element orders can appear in a group of given order

# Construction / Recognition

## To Apply:
1. Determine $|G|$
2. Find the order of the element $x$
3. Verify that the order divides $|G|$

# Context & Application

Armstrong uses this corollary to prove that groups of prime order are cyclic (Corollary 11.3), and to show that $A_4$ has no subgroup of order 6 — since a 3-cycle cannot belong to a group of order 4, as 3 does not divide 4.

# Examples

**Example 1** (p. 65): In $A_4$ (order 12), element orders must divide 12. The identity has order 1, double transpositions have order 2, and 3-cycles have order 3.

**Example 2** (p. 65): A 3-cycle cannot belong to a group of order 4 because 3 does not divide 4.

# Relationships

## Builds Upon
- **Lagrange's theorem** — Direct corollary

## Enables
- **Groups of prime order are cyclic** — Any non-identity element generates the whole group
- **$x^{|G|} = e$** — Corollary (11.4)

# Common Errors

- **Error**: Assuming every divisor of $|G|$ occurs as an element order
  **Correction**: Not every divisor of $|G|$ need appear as the order of an element

# Common Confusions

- **Confusion**: Thinking this result is the same as Cauchy's theorem
  **Clarification**: This result says element orders divide $|G|$; Cauchy's theorem says if a prime $p$ divides $|G|$, then some element has order $p$. The directions are opposite.

# Source Reference

Chapter 11: Lagrange's Theorem, Corollary (11.2), p. 65 (pdf).

# Verification Notes

- Definition source: Direct from Corollary (11.2)
- Confidence rationale: HIGH — explicit corollary with proof
- Uncertainties: None
