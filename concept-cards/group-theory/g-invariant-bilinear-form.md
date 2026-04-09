---
# === CORE IDENTIFICATION ===
concept: G-invariant Bilinear Form
slug: g-invariant-bilinear-form

# === CLASSIFICATION ===
category: representation-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 102
section: "Maschke's theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "invariant bilinear form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
  - g-invariant-subspace
extends: []
related:
  - maschke-theorem
  - unitary-representation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a G-invariant bilinear form?"
  - "How do G-invariant bilinear forms help decompose representations?"
---

# Quick Definition

A bilinear form phi: V x V -> F is G-invariant if phi(gv, gv') = phi(v, v') for all g in G and v, v' in V.

# Core Definition

A bilinear form phi: V x V -> F is said to be **G-invariant** if phi(gv, gv') = phi(v, v') for all g in G, v, v' in V. (Milne, Chapter 7, p. 102)

# Prerequisites

- **Linear representation** — the group G acts linearly on V
- **G-invariant subspace** — orthogonal complements of G-invariant subspaces with respect to G-invariant forms are also G-invariant

# Key Properties

1. If phi is G-invariant and W is a G-invariant subspace, then W^perp is also G-invariant (Lemma 7.5)
2. Averaging any symmetric bilinear form phi over G produces a G-invariant form: phi_bar(v,w) = sum_{g in G} phi(gv, gw) (Lemma 7.6)
3. If phi is positive definite (over R), the averaged form phi_bar is also positive definite (Lemma 7.7)

# Construction / Recognition

1. Start with any symmetric bilinear form phi on V
2. Average over G: phi_bar(v,w) = sum_{g in G} phi(gv, gw)
3. The result is G-invariant
4. If the original form was positive definite (over R or C), the averaged form is too

# Context & Application

G-invariant bilinear forms are the key tool in the first proof of Maschke's theorem over R and C. If V has a G-invariant positive definite symmetric bilinear form, then every G-invariant subspace has a G-invariant orthogonal complement, proving complete reducibility.

# Examples

**Example 1** (p. 103, Lemma 7.6): Starting from any symmetric bilinear form phi on V, the averaged form phi_bar(v,w) = sum_{g in G} phi(gv, gw) is G-invariant.

# Relationships

## Builds Upon
- **linear-representation** — defined on the space of a representation

## Enables
- **maschke-theorem** — first proof uses G-invariant positive definite forms
- **unitary-representation** — defined by existence of G-invariant positive definite form

## Related
- **g-invariant-subspace** — orthogonal complements w.r.t. invariant forms are invariant

## Contrasts With
- Non-invariant bilinear forms

# Common Errors

- **Error**: Assuming the averaged form is always nondegenerate
  **Correction**: The averaged form need not be nondegenerate in general (p. 103); positive definiteness (over R) guarantees nondegeneracy

# Common Confusions

- **Confusion**: Thinking any G-invariant form suffices for Maschke's theorem
  **Clarification**: The form must be nondegenerate (or positive definite) for the orthogonal complement to give a direct sum decomposition

# Source Reference

Chapter 7: Representations of Finite Groups, pp. 102-103 (Lemmas 7.5-7.7).

# Verification Notes

- Definition source: Direct from p. 102
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
