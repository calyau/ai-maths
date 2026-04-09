---
# === CORE IDENTIFICATION ===
concept: Bijective Function
slug: bijective-function

# === CLASSIFICATION ===
category: foundations
subcategory: set-theory
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Preliminaries"
chapter_number: 1
pdf_page: 20
section: "Cartesian Products and Mappings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bijection
  - one-to-one correspondence

# === TYPED RELATIONSHIPS ===
prerequisites:
  - injective-function
  - surjective-function
extends:
  - injective-function
  - surjective-function
related:
  - inverse-mapping
  - permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A map that is both one-to-one (injective) and onto (surjective) is called bijective. Bijective maps establish a one-to-one correspondence between domain and codomain.

# Core Definition

"A map that is both one-to-one and onto is called bijective" (Judson, p. 20). A bijective function $f: A \to B$ pairs each element of $A$ with exactly one element of $B$, and every element of $B$ is paired with exactly one element of $A$.

# Prerequisites

- **Injective function** — A bijection must be one-to-one
- **Surjective function** — A bijection must be onto

# Key Properties

1. Combines injectivity and surjectivity
2. A mapping is invertible if and only if it is bijective (Theorem 1.20)
3. The composition of two bijective maps is bijective (Theorem 1.15)

# Construction / Recognition

## To Prove Bijectivity:
1. Prove injectivity: show $f(a_1) = f(a_2)$ implies $a_1 = a_2$
2. Prove surjectivity: show for every $b \in B$, there exists $a \in A$ with $f(a) = b$

# Context & Application

Bijections are essential in abstract algebra: group isomorphisms are bijective homomorphisms, and permutations are bijections from a set to itself. A map is invertible if and only if it is bijective.

# Examples

**Example 1** (p. 20): The map $\pi: S \to S$ where $S = \{1, 2, 3\}$ defined by $\pi(1) = 2$, $\pi(2) = 1$, $\pi(3) = 3$ is bijective.

# Relationships

## Builds Upon
- **injective-function** — Bijection requires injectivity
- **surjective-function** — Bijection requires surjectivity

## Enables
- **inverse-mapping** — Bijective maps are exactly the invertible maps
- **permutation** — Permutations are bijections from a set to itself

# Common Errors

- **Error**: Proving only one of injectivity or surjectivity and claiming bijectivity
  **Correction**: Both properties must be established

# Common Confusions

- **Confusion**: Thinking all injective maps are bijective
  **Clarification**: An injective map $f: A \to B$ is bijective only if it is also surjective (i.e., $f(A) = B$)

# Source Reference

Chapter 1: Preliminaries, Section 1.2, page 20. Theorem 1.15, page 22.

# Verification Notes

- Definition source: Direct from p. 20
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
