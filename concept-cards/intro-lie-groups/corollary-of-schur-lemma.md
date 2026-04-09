---
# === CORE IDENTIFICATION ===
concept: "Schur's Lemma Corollary: Decomposition of Intertwining Operators"
slug: corollary-of-schur-lemma

# === CLASSIFICATION ===
category: representations
subcategory: irreducibility
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 43
section: "4.4 Intertwining operators and Schur lemma"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - schur-lemma
  - completely-reducible-representation
extends:
  - schur-lemma
related:
  - decomposition-using-central-elements
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do intertwining operators behave on completely reducible representations?"
---

# Quick Definition

For a completely reducible representation $V = \bigoplus n_i V_i$ with $V_i$ pairwise non-isomorphic irreducibles, any intertwining operator takes the block-diagonal form $\Phi = \bigoplus (A_i \otimes \mathrm{id}_{V_i})$ where $A_i \in \mathrm{End}(\mathbb{C}^{n_i})$.

# Core Definition

**Corollary 4.24** (Kirillov, p. 43):

1. If $V = \bigoplus V_i$ with $V_i$ irreducible, pairwise non-isomorphic, then any intertwining operator $\Phi: V \to V$ is $\Phi = \bigoplus \lambda_i\,\mathrm{id}_{V_i}$.
2. If $V = \bigoplus n_i V_i = \bigoplus \mathbb{C}^{n_i} \otimes V_i$, then $\Phi = \bigoplus (A_i \otimes \mathrm{id}_{V_i})$ with $A_i \in \mathrm{End}(\mathbb{C}^{n_i})$.

# Prerequisites

- **Schur's lemma** — The foundation: intertwiners between different irreducibles vanish
- **Completely reducible representation** — Needed for the block decomposition

# Key Properties

1. When all multiplicities are 1: intertwiners are diagonal (scalar on each irreducible)
2. Each eigenvalue appears with multiplicity $\dim V_i$
3. For the general case: the intertwiner can mix copies of the same irreducible but not different ones

# Context & Application

This is the precise mechanism by which decomposing a representation into irreducibles simplifies the analysis of invariant operators. In quantum mechanics, symmetry-adapted observables have this block structure.

# Examples

**Example** (p. 44): If $V = \bigoplus V_i$ with all $V_i$ pairwise non-isomorphic, finding $\Phi(v)$ for one vector in each $V_i$ determines $\Phi$ completely: $\lambda_i = \Phi(v)/v$ on $V_i$.

# Relationships

## Builds Upon
- **Schur's lemma** — Off-diagonal blocks vanish

## Enables
- **Practical decomposition** — Computing intertwiners reduces to scalar/block-diagonal computation

# Source Reference

Chapter 4, Section 4.4, Corollary 4.24, pp. 43-44.

# Verification Notes

- Definition source: Direct from Corollary 4.24
- Confidence rationale: Explicit corollary
- Uncertainties: None
- Cross-reference status: Verified
