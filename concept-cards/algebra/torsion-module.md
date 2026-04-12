---
concept: Torsion Module
slug: torsion-module
category: module-theory
subcategory: module-types
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Algebra in a Ring"
chapter_number: 14
pdf_page: 432
section: "14.7 Structure of Abelian Groups"
extraction_confidence: medium
aliases:
  - "torsion element"
prerequisites:
  - module
extends: []
related:
  - free-module
  - structure-theorem-finitely-generated-modules-pid
contrasts_with:
  - free-module
answers_questions:
  - "What is a torsion module?"
  - "What is a torsion element?"
---

# Quick Definition

A torsion element of a module V over an integral domain R is a nonzero element v such that rv = 0 for some nonzero r in R. A torsion module is one in which every element is a torsion element.

# Core Definition

In the structure theorem decomposition V = C_{d_1} + ... + C_{d_k} + L, the torsion submodule consists of the cyclic summands C_{d_i}, and L is the free (torsion-free) part. For abelian groups (Z-modules), an element v has torsion if nv = 0 for some positive integer n. The structure theorem separates the torsion part from the free part (Artin, Theorem 14.7.3).

# Prerequisites

- **Module** -- Torsion is a property of module elements

# Key Properties

1. In the structure theorem, V = (torsion part) + (free part)
2. Over Z, a finite abelian group is entirely torsion
3. An element v with d_i*v = 0 contributes to the cyclic summand C_{d_i}
4. The torsion submodule is the kernel of the map V -> V tensor Q (for Z-modules)

# Context & Application

The torsion/free decomposition is one of the key features of the structure theorem. It separates the "finite order" behavior from the "infinite order" behavior in finitely generated modules.

# Examples

**Example 1** (p. 443): In Z/4Z + Z, the element (1, 0) has torsion (4 times it is 0), while (0, 1) is torsion-free.

# Relationships

## Contrasts With
- **Free module** -- Torsion-free modules with a basis

## Related
- **Structure theorem for finitely generated modules over a PID** -- Separates torsion from free parts

# Source Reference

Chapter 14: Linear Algebra in a Ring, Section 14.7, pages 443-448.

# Verification Notes

- Definition source: Synthesized from Artin's structure theorem treatment
- Confidence rationale: Concept is implicit in the structure theorem discussion
- Uncertainties: Artin does not give a standalone definition; synthesized from context
- Cross-reference status: Verified
