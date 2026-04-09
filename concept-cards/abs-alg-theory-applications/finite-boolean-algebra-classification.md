---
# === CORE IDENTIFICATION ===
concept: Classification of Finite Boolean Algebras
slug: finite-boolean-algebra-classification

# === CLASSIFICATION ===
category: lattice-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Lattices and Boolean Algebras"
chapter_number: 19
pdf_page: 259
section: "19.2 Boolean Algebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - boolean-algebra
  - atom-boolean-algebra
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What do finite Boolean algebras look like?"
  - "How are finite Boolean algebras classified?"
---

# Quick Definition

Every finite Boolean algebra is isomorphic to the power set $\mathcal{P}(X)$ of a finite set $X$, where $X$ is the set of atoms. Consequently, every finite Boolean algebra has order $2^n$ for some $n$.

# Core Definition

"Let $B$ be a finite Boolean algebra. Then there exists a set $X$ such that $B$ is isomorphic to $\mathcal{P}(X)$" (Judson, Theorem 19.23, p. 259). The isomorphism $\phi : B \to \mathcal{P}(X)$ maps each element $b = a_1 \vee \cdots \vee a_n$ to $\{a_1, \ldots, a_n\}$ where $a_i$ are the atoms below $b$.

# Prerequisites

- **Boolean algebra** — The result classifies finite Boolean algebras
- **Atom** — The set $X$ consists of atoms

# Key Properties

1. Every finite Boolean algebra $\cong \mathcal{P}(X)$ for $X$ = set of atoms
2. $|B| = 2^n$ where $n$ = number of atoms (Corollary 19.24)
3. The isomorphism maps $b \mapsto \{$atoms $a : a \preceq b\}$
4. Preserves $\vee$ (maps to $\cup$) and $\wedge$ (maps to $\cap$)

# Construction / Recognition

## To Apply:
1. Find all atoms of $B$
2. Map each element to its set of atoms below it
3. This gives an isomorphism $B \cong \mathcal{P}(X)$

# Context & Application

This is a complete classification theorem: it says finite Boolean algebras are fully determined by their number of atoms. This simplifies both theoretical work and applications (e.g., circuit design).

# Examples

**Example 1**: A Boolean algebra with 3 atoms is isomorphic to $\mathcal{P}(\{a,b,c\})$ and has $2^3 = 8$ elements.

**Example 2**: The divisors of $30 = 2 \cdot 3 \cdot 5$ under divisibility form a Boolean algebra with atoms $2, 3, 5$, isomorphic to $\mathcal{P}(\{2,3,5\})$.

# Relationships

## Builds Upon
- **Atom** — Atoms determine the structure
- **Boolean algebra** — The objects being classified

# Common Errors

- **Error**: Expecting Boolean algebras of arbitrary finite size
  **Correction**: The order must be a power of 2

# Common Confusions

- **Confusion**: Thinking different sets of atoms can give non-isomorphic Boolean algebras of the same size
  **Clarification**: All Boolean algebras with $n$ atoms are isomorphic to $\mathcal{P}(\{1,\ldots,n\})$

# Source Reference

Chapter 19: Lattices and Boolean Algebras, Section 19.2, Theorem 19.23 and Corollary 19.24, pages 259-260.

# Verification Notes

- Definition source: Direct from Theorem 19.23
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
