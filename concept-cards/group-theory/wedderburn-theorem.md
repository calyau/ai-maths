---
# === CORE IDENTIFICATION ===
concept: "Wedderburn's Theorem (Structure of Simple Algebras)"
slug: wedderburn-theorem

# === CLASSIFICATION ===
category: module-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Representations of Finite Groups"
chapter_number: 7
pdf_page: 109
section: "Simple F-algebras and their modules"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Wedderburn structure theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - simple-f-algebra
  - division-algebra
  - schur-lemma
  - double-centralizer-theorem
extends: []
related:
  - wedderburn-artin-theorem
  - matrix-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the structure of a simple F-algebra?"
  - "How does Wedderburn's theorem classify simple algebras?"
---

# Quick Definition

Every simple F-algebra is isomorphic to M_n(D) for some positive integer n and some division F-algebra D. Both n and D (up to isomorphism) are uniquely determined.

# Core Definition

**Theorem 7.25.** Every simple F-algebra is isomorphic to M_n(D) for some n and some division F-algebra D. (Milne, Theorem 7.25, p. 109)

The proof proceeds: choose a simple A-module S (e.g., a minimal left ideal). A acts faithfully on S. Let D = C(A) in End_F(S). By the double centralizer theorem, A = End_D(S). By Schur's lemma, D is a division algebra. Since S is a free D-module of rank n, A = End_D(D^n) = M_n(D^opp).

# Prerequisites

- **Simple F-algebra** — the theorem classifies these
- **Division algebra** — the building block
- **Schur's lemma** — shows the centralizer is a division algebra
- **Double centralizer theorem** — shows A = End_D(S)

# Key Properties

1. n is uniquely determined by A (7.30): n = dim_D(S) for any simple module S
2. D is uniquely determined up to isomorphism (7.30): D^opp = End_A(S)
3. Over an algebraically closed field, D = F, so every simple F-algebra is M_n(F)
4. Every simple F-algebra is semisimple (7.26)
5. Any two simple modules over M_n(D) are isomorphic (7.27)

# Construction / Recognition

Given a simple F-algebra A:
1. Find a simple A-module S (a minimal left ideal)
2. Compute D = End_A(S) (a division algebra by Schur's lemma)
3. Then A = M_n(D^opp) where n = dim_D(S)

# Context & Application

Wedderburn's theorem is the cornerstone of the structure theory of algebras. Together with the Wedderburn-Artin theorem (semisimple = product of simples), it gives a complete description of semisimple algebras. For the group algebra F[G] over an algebraically closed field, each simple factor is M_{f_i}(F).

# Examples

**Example 1** (p. 108): M_n(D) is simple for any division algebra D, and conversely every simple algebra has this form.

**Example 2** (p. 110): Over an algebraically closed field, every simple algebra is M_n(F) since D = F (7.31).

# Relationships

## Builds Upon
- **simple-f-algebra** — classifies these
- **double-centralizer-theorem** — key proof technique
- **schur-lemma** — shows centralizer is a division algebra

## Enables
- **wedderburn-artin-theorem** — combined with product decomposition
- **decomposition-of-f-g** — F[G] = product of M_{f_i}(F)

## Related
- **matrix-algebra** — the general form of a simple algebra

## Contrasts With
- Structure of non-simple algebras

# Source Reference

Chapter 7: Representations of Finite Groups, Theorem 7.25 and Corollary 7.30, pp. 109-110.

# Verification Notes

- Definition source: Direct from Theorem 7.25
- Confidence rationale: HIGH — explicit named theorem with proof
- Uncertainties: None
