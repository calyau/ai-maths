---
# === CORE IDENTIFICATION ===
concept: Right-Invariant Vector Field
slug: right-invariant-vector-field

# === CLASSIFICATION ===
category: lie-groups
subcategory: group-actions
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 14
section: "2.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
  - right-action
extends: []
related:
  - left-invariant-vector-field
  - lie-algebra
  - commutator-bracket
contrasts_with:
  - left-invariant-vector-field

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie algebra?"
  - "How does a Lie algebra relate to its Lie group?"
---

# Quick Definition

A right-invariant vector field on $G$ satisfies $v.g = v$ for all $g \in G$. The isomorphism $\mathfrak{g} \cong \{\text{right-invariant fields}\}$ via $v \mapsto v(1)$ is an isomorphism of Lie algebras (Corollary 3.25).

# Core Definition

**Definition 2.24** (Kirillov): A vector field $v \in \mathrm{Vect}(G)$ is right-invariant if $v.g = v$ for every $g \in G$.

**Corollary 3.25**: The isomorphism $\mathfrak{g} \cong \{\text{right-invariant vector fields on } G\}$ defined in Theorem 2.25 is an isomorphism of Lie algebras.

# Prerequisites

- **Lie group** — the group on which fields live
- **Right action** — invariance is with respect to right multiplication

# Key Properties

1. Every $x \in T_1G$ extends uniquely to a right-invariant field via $v(g) = xg$.
2. The Lie bracket of right-invariant fields equals the Lie algebra bracket (Corollary 3.25).
3. The flow of the right-invariant field for $x$ is $g \mapsto \exp(tx)g$ (Proposition 3.6 part 2).
4. Contrast: left-invariant fields give the negative bracket (Exercise 3.4).

# Construction / Recognition

## To Construct/Create:
1. Choose $x \in T_1G$.
2. Define $v(g) = xg$ (right multiplication by $g$ on $x$).

## To Identify/Recognize:
1. A vector field invariant under all right translations.

# Context & Application

Right-invariant vector fields are preferred for the Lie algebra bracket because their commutator equals (not the negative of) the Lie algebra bracket. They are used in the proof of Theorem 3.43 via Frobenius.

# Examples

**Proposition 3.24** (p. 27): The left multiplication action $L(g).h = gh$ gives rise to right-invariant vector fields: $\xi(g) = xg$ for $x \in \mathfrak{g}$.

# Relationships

## Builds Upon
- **Right action** — the invariance condition

## Enables
- **Lie algebra bracket** — the bracket of right-invariant fields equals $[x, y]$
- **Frobenius application** — right-invariant fields closed under bracket prove Theorem 3.43

## Contrasts With
- **Left-invariant vector field** — bracket of left-invariant fields gives $-[x, y]$

# Common Errors

- **Error**: Using left-invariant fields and expecting the standard bracket sign.
  **Correction**: Left-invariant fields give $[\xi^x, \xi^y] = -\xi^{[x,y]}$ (Exercise 3.4). Use right-invariant for the correct sign.

# Common Confusions

- **Confusion**: Why the sign difference between left and right.
  **Clarification**: It comes from the inverse in the definition of the action on functions: $(\rho(g)f)(m) = f(g^{-1}m)$ (Remark 3.21).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.4, Definition 2.24, Theorem 2.25. Chapter 3, Corollary 3.25, Proposition 3.24.

# Verification Notes

- Definition source: Direct from Definition 2.24
- Confidence rationale: Explicit definition and Corollary 3.25
- Uncertainties: None
- Cross-reference status: Verified with Corollary 3.25, Proposition 3.24, Exercise 3.4
