---
# === CORE IDENTIFICATION ===
concept: Unitary Representation
slug: unitary-representation

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
pdf_page: 103
section: "Maschke's theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linear-representation
  - g-invariant-bilinear-form
extends:
  - linear-representation
related:
  - maschke-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a unitary representation?"
  - "When is a representation unitary?"
---

# Quick Definition

A representation of G on a real vector space V is unitary if there exists a G-invariant positive definite symmetric bilinear form on V.

# Core Definition

A representation of a group G on a real vector space V is **unitary** if there exists a G-invariant positive definite symmetric bilinear form on V. Every unitary representation is semisimple (Lemma 7.5), and every real representation of a finite group is unitary (Lemma 7.7). (Milne, Aside 7.8, p. 103)

# Prerequisites

- **Linear representation** — unitary is a property of representations
- **G-invariant bilinear form** — the form must be G-invariant and positive definite

# Key Properties

1. Every unitary representation is semisimple (7.5)
2. Every real representation of a finite group is unitary (7.7)
3. The G-invariant form is constructed by averaging any positive definite form over G

# Construction / Recognition

1. Start with any positive definite symmetric bilinear form phi on V
2. Average: phi_bar(v,w) = sum_{g in G} phi(gv, gw)
3. phi_bar is G-invariant and positive definite
4. Therefore V is unitary

# Context & Application

Unitarity provides the conceptual explanation for why real and complex representations of finite groups are completely reducible: the orthogonal complement of any G-invariant subspace (with respect to the invariant form) is again G-invariant.

# Examples

**Example 1** (p. 103): Every representation of a finite group over R is unitary, by averaging any positive definite form.

# Relationships

## Builds Upon
- **linear-representation** — unitary is a special type of representation
- **g-invariant-bilinear-form** — the defining feature

## Enables
- Understanding why Maschke's theorem works over R and C

## Related
- **maschke-theorem** — unitarity implies the first proof of Maschke's theorem

## Contrasts With
- Representations over fields where positive definiteness does not make sense

# Common Errors

- **Error**: Thinking unitarity is needed for Maschke's theorem in general
  **Correction**: The general proof of Maschke's theorem uses averaged projectors, not bilinear forms

# Common Confusions

- **Confusion**: Confusing "unitary" in this context with the usual sense of unitary matrices
  **Clarification**: Here "unitary" means admitting a G-invariant positive definite form; over C one would use Hermitian forms

# Source Reference

Chapter 7: Representations of Finite Groups, Aside 7.8, p. 103.

# Verification Notes

- Definition source: Direct from Aside 7.8
- Confidence rationale: HIGH — explicit definition
- Uncertainties: None
