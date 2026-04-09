---
# === CORE IDENTIFICATION ===
concept: Left Action
slug: left-action

# === CLASSIFICATION ===
category: lie-groups
subcategory: group-actions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 13
section: "2.4"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "left multiplication"
  - "left translation"
  - "$L_g$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - right-action
  - adjoint-action-on-lie-group
  - left-invariant-vector-field
contrasts_with:
  - right-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
---

# Quick Definition

The left action of a Lie group $G$ on itself is given by $L_g(h) = gh$, i.e., left multiplication by $g$. It is a simply transitive action.

# Core Definition

(Kirillov, p. 13): Left action: $L_g: G \to G$ is defined by $L_g(h) = gh$.

# Prerequisites

- **Lie group** — the group acting on itself

# Key Properties

1. The left action is simply transitive: for any $h_1, h_2 \in G$, there is a unique $g = h_2 h_1^{-1}$ with $L_g(h_1) = h_2$.
2. Left and right actions commute: $L_g \circ R_h = R_h \circ L_g$.
3. $\mathrm{Ad}_g = L_g \circ R_g$ (adjoint is the composition of left and right actions).
4. For matrix groups, $(L_g)_* v = gv$ (ordinary matrix multiplication) (Exercise 2.6).

# Construction / Recognition

## To Construct/Create:
1. For $g \in G$, define $L_g: G \to G$ by $L_g(h) = gh$.

## To Identify/Recognize:
1. Multiplication on the left by a fixed group element.

# Context & Application

The left action is used to define left-invariant vector fields and to transport tangent vectors from the identity to any other point of the group.

# Examples

**Example** (p. 14): For $G = \mathrm{GL}(n, \mathbb{R})$, the left action is $L_A(B) = AB$, and $(L_A)_* v = Av$ for $v \in T_B G$.

# Relationships

## Builds Upon
- **Lie group** — acts on itself

## Enables
- **Left-invariant vector field** — defined by invariance under left action

## Related
- **Right action** — the other fundamental action of $G$ on itself

## Contrasts With
- **Right action** — $R_g(h) = hg^{-1}$; note the inverse

# Common Errors

- **Error**: Confusing left and right actions.
  **Correction**: Left action is $L_g(h) = gh$; right action is $R_g(h) = hg^{-1}$ (note the inverse to make it a left group action).

# Common Confusions

- **Confusion**: Why the right action uses $g^{-1}$.
  **Clarification**: To make $R: G \to \mathrm{Diff}(G)$ a group homomorphism (not anti-homomorphism), we need $R_g(h) = hg^{-1}$.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.4, page 13.

# Verification Notes

- Definition source: Direct from source
- Confidence rationale: Explicit definition in source
- Uncertainties: None
- Cross-reference status: Verified with Exercise 2.6
