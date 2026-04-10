---
concept: Isogeny Theorem
slug: isogeny-theorem
category: reductive-groups
subcategory: null
tier: advanced
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: The Split Case"
chapter_number: 5
pdf_page: 377
section: "Construction of isogenies of split reductive groups"
extraction_confidence: high
aliases: []
prerequisites:
  - root-datum
  - split-reductive-group
extends: []
related:
  - isomorphism-theorem-reductive-groups
  - existence-theorem-reductive-groups
contrasts_with: []
answers_questions:
  - "What is the isogeny theorem?"
---

# Quick Definition

The isogeny theorem states that every isogeny of root data arises from an isogeny of split reductive groups. An isogeny of root data is a map φ: X' → X that is injective with finite cokernel and sends roots to root multiples.

# Core Definition

An **isogeny of root data** is a homomorphism φ: X' → X such that (a) both φ and φ^∨ are injective, and (b) there is a bijection α ↦ α' from R to R' and positive integers q(α) (powers of the characteristic exponent) such that φ(α') = q(α)α and φ^∨(α^∨) = q(α)(α')^∨ (Milne, Definition 7.1, p. 377).

**Theorem 7.4 (Isogeny Theorem)**: Let (G,T) and (G',T') be split reductive groups. Every isogeny of their root data φ: X(T') → X(T) arises from an isogeny f: (G,T) → (G',T').

# Prerequisites

- **Root datum** — Isogenies are maps between root data
- **Split reductive group** — The groups involved

# Key Properties

1. In characteristic 0, q(α) = 1 for all α (only "central" isogenies)
2. The isogeny is determined up to conjugation by T/Z (Lemma 7.3)
3. Specializes to the isomorphism theorem when φ is an isomorphism

# Source Reference

Chapter V, Section 7, Theorems 7.4–7.6, pages 377–378.

# Verification Notes

- Definition source: Direct from Definition 7.1 and Theorem 7.4
- Confidence: HIGH
- Uncertainties: None
