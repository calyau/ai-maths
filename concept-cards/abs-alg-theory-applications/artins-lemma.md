---
# === CORE IDENTIFICATION ===
concept: Artin's Lemma
slug: artins-lemma

# === CLASSIFICATION ===
category: galois-theory
subcategory: field-automorphisms
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Galois Theory"
chapter_number: 23
pdf_page: 307
section: "23.2 The Fundamental Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - fixed-field
  - field-automorphism
extends: []
related:
  - fundamental-theorem-of-galois-theory
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does Artin's Lemma say about the degree of a field over a fixed field?"
---

# Quick Definition

Artin's Lemma states that if $G$ is a finite group of automorphisms of a field $E$ and $F = E_G$ is the fixed field, then $[E:F] \leq |G|$.

# Core Definition

**Lemma 23.18 (Artin's Lemma).** Let $G$ be a finite group of automorphisms of $E$ and let $F = E_G$. Then $[E:F] \leq |G|$ (Judson, p. 312).

The proof shows that any set of $|G| + 1$ elements must be linearly dependent over $F$ by using a system of homogeneous linear equations involving the automorphisms.

# Prerequisites

- **Fixed field** — The lemma bounds the degree relative to the fixed field
- **Field automorphism** — The group consists of automorphisms

# Key Properties

1. The bound $[E:F] \leq |G|$ is sharp: equality holds for Galois extensions
2. The proof uses linear algebra: more unknowns than equations guarantees a nontrivial solution
3. Combined with $|G(E/F)| = [E:F]$ (Theorem 23.7), gives $[E:F] = |G|$ for Galois extensions
4. The proof is due to Emil Artin

# Context & Application

Artin's Lemma is a crucial step in proving the Fundamental Theorem of Galois Theory. It provides the bound that, together with other results, establishes the equality $[E:F] = |G(E/F)|$.

# Relationships

## Builds Upon
- **Fixed field** — Bounds the degree over the fixed field
- **Field automorphism** — Uses a group of automorphisms

## Enables
- **Fundamental Theorem of Galois Theory** — Key ingredient in the proof

# Source Reference

Chapter 23: Galois Theory, Section 23.2, pages 312–313. Lemma 23.18.

# Verification Notes

- Definition source: Direct from Lemma 23.18, p. 312
- Confidence: HIGH — explicit lemma with proof
- Cross-reference status: Verified
- Uncertainties: None
