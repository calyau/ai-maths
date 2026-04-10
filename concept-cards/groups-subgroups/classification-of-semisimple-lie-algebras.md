---
concept: Classification of Semisimple Lie Algebras
slug: classification-of-semisimple-lie-algebras
category: semisimple-theory
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 314
section: "Classification of split semisimple Lie algebras"
extraction_confidence: high
aliases: []
prerequisites:
  - root-system
  - dynkin-diagram
  - split-semisimple-lie-algebra
extends: []
related:
  - simply-connected-algebraic-group
  - adjoint-algebraic-group
contrasts_with: []
answers_questions:
  - "How do root systems classify semisimple Lie algebras?"
---

# Quick Definition

Split semisimple Lie algebras over a field of characteristic zero are classified (up to isomorphism) by their root systems, which in turn are classified by Dynkin diagrams. Every root system arises, and the root system determines the algebra uniquely.

# Core Definition

Two classification theorems (Milne, §2j, p. 314):

1. **Existence** (Theorem 2.35): Every root system over k arises from a split semisimple Lie algebra over k.
2. **Isomorphism** (Theorem 2.36): The root system of a split semisimple Lie algebra determines it up to isomorphism.

Combined with the classification of root systems by Dynkin diagrams (Theorem 1.17), this gives a complete classification.

# Prerequisites

- **Root system** — The classifying invariant
- **Dynkin diagram** — Classifies indecomposable root systems
- **Split semisimple Lie algebra** — The objects being classified

# Key Properties

1. Simple Lie algebras correspond to indecomposable root systems (Proposition 2.32)
2. The classification types are: A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2
3. The isomorphism in Theorem 2.36 is unique once bases and root vectors are chosen

# Context & Application

This classification is the foundation for the classification of semisimple algebraic groups. For algebraic groups, one additionally needs to specify a lattice X between Q and P.

# Examples

**Example 1** (p. 311): sl_{n+1} has root system A_n and is simple (Dynkin diagram connected, Corollary 2.27).

# Source Reference

Chapter III, Section 2j, Theorems 2.35–2.36, pages 314–315.

# Verification Notes

- Definition source: Direct from Theorems 2.35 and 2.36
- Confidence: HIGH — major theorems stated explicitly
- Uncertainties: None
