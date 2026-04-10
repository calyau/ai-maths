---
concept: Inverse Root System
slug: inverse-root-system
category: root-systems
subcategory: null
tier: intermediate
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Semisimple Lie Algebras and Algebraic Groups in Characteristic Zero"
chapter_number: 3
pdf_page: 303
section: "The root and weight lattices"
extraction_confidence: high
aliases:
  - "dual root system"
  - "R^∨"
  - "coroot system"
prerequisites:
  - root-system
  - coroot
extends: []
related:
  - weight-lattice
  - root-datum
contrasts_with: []
answers_questions:
  - "What is the inverse root system?"
---

# Quick Definition

The inverse (or dual) root system R^∨ = {α^∨ | α ∈ R} is a root system in V^∨ obtained by collecting all the coroots. It has the same Weyl group as R but with long and short roots interchanged.

# Core Definition

Let (V, R) be a root system. The set R^∨ = {α^∨ | α ∈ R} is a root system in V^∨, called the **inverse root system** (Milne, 1.19, p. 303). If S is a base for R, then S^∨ = {α^∨ | α ∈ S} is a base for R^∨ (1.21).

# Prerequisites

- **Root system** — The original root system
- **Coroot** — The elements of R^∨

# Key Properties

1. R^∨ is a root system in V^∨
2. W(R) = W(R^∨) (same Weyl group)
3. Long roots of R correspond to short coroots of R^∨ and vice versa
4. The dual of a type B_n root system is type C_n

# Source Reference

Chapter III, Section 1i, 1.19, page 303.

# Verification Notes

- Definition source: Direct from 1.19
- Confidence: HIGH
- Uncertainties: None
