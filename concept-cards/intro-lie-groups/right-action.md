---
# === CORE IDENTIFICATION ===
concept: Right Action
slug: right-action

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
  - "right multiplication"
  - "right translation"
  - "$R_g$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - left-action
  - adjoint-action-on-lie-group
  - right-invariant-vector-field
contrasts_with:
  - left-action

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Lie group?"
---

# Quick Definition

The right action of a Lie group $G$ on itself is given by $R_g(h) = hg^{-1}$. It is simply transitive and commutes with the left action.

# Core Definition

(Kirillov, p. 13): Right action: $R_g: G \to G$ is defined by $R_g(h) = hg^{-1}$.

# Prerequisites

- **Lie group** — the group acting on itself

# Key Properties

1. Simply transitive, like the left action.
2. Commutes with left action: $L_g \circ R_h = R_h \circ L_g$.
3. For matrix groups, $(R_{g^{-1}})_* v = vg$ (Exercise 2.6), so we write $vg$ for $(R_{g^{-1}})_* v$.

# Construction / Recognition

## To Construct/Create:
1. For $g \in G$, define $R_g(h) = hg^{-1}$.

## To Identify/Recognize:
1. Multiplication on the right by $g^{-1}$.

# Context & Application

The right action defines right-invariant vector fields, which play a key role in the correspondence between the Lie algebra and the group (Corollary 3.25).

# Examples

**Example** (p. 14): For $G = \mathrm{GL}(n, \mathbb{R})$, $R_g(h) = hg^{-1}$ and $(R_{g^{-1}})_* v = vg$.

# Relationships

## Builds Upon
- **Lie group** — acts on itself

## Enables
- **Right-invariant vector field** — defined by invariance under right action

## Related
- **Adjoint action on Lie group** — $\mathrm{Ad}_g = L_g \circ R_g$

## Contrasts With
- **Left action** — $L_g(h) = gh$ vs $R_g(h) = hg^{-1}$

# Common Errors

- **Error**: Writing the right action as $R_g(h) = hg$ instead of $hg^{-1}$.
  **Correction**: The inverse is needed so that $g \mapsto R_g$ is a group homomorphism.

# Common Confusions

- **Confusion**: Whether right-invariant or left-invariant fields correspond to the Lie algebra bracket.
  **Clarification**: Right-invariant vector fields give a Lie algebra isomorphic to $\mathfrak{g}$ with the standard bracket (Corollary 3.25); left-invariant fields give the bracket with opposite sign (Exercise 3.4).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.4, page 13.

# Verification Notes

- Definition source: Direct from source
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified with Exercise 2.6, Corollary 3.25
