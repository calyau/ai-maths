---
concept: Conjugation
slug: conjugation
category: group-theory
subcategory: conjugation
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.2 The Class Equation"
extraction_confidence: high
aliases:
  - "conjugation action"
prerequisites:
  - group-action
extends:
  - group-action
related:
  - conjugacy-class
  - centralizer
  - normalizer
contrasts_with:
  - cayleys-theorem
answers_questions:
  - "What is conjugation as a group action?"
---

# Quick Definition

Conjugation is the action of G on itself defined by (g, x) -> gxg^{-1}. It is the most important group operation, more subtle than left multiplication. Its orbits are conjugacy classes and its stabilizers are centralizers.

# Core Definition

Conjugation is the operation of G on itself defined by (g, x) -> gxg^{-1} (Artin, (7.2.1), p. 207). The associative law (gh)*x = g*(h*x) is verified by (gh)x(gh)^{-1} = g(hxh^{-1})g^{-1}. Orbits are conjugacy classes; stabilizers are centralizers.

# Prerequisites

- **Group action** — Conjugation is a specific group action

# Key Properties

1. Orbits = conjugacy classes
2. Stabilizers = centralizers
3. Fixed points = elements of the center
4. Also acts on the set of subgroups (stabilizer = normalizer)
5. Preserves order of elements

# Context & Application

Artin describes conjugation as "more subtle and more important than left multiplication." It reveals the internal structure of a group through conjugacy classes, the class equation, and the distinction between normal and non-normal subgroups.

# Examples

**Example 1** (p. 207): In S_n, conjugation by q relabels: qpq^{-1} replaces indices according to q.

**Example 2** (p. 207): In S_3, conjugation of x by y gives yxy^{-1} = x^2.

# Relationships

## Builds Upon
- **Group action** — Conjugation is a group action

## Enables
- **Conjugacy class** — Orbits of conjugation
- **Centralizer** — Stabilizer for conjugation on elements
- **Normalizer** — Stabilizer for conjugation on subgroups
- **Class equation** — From the orbit decomposition

## Contrasts With
- **Left multiplication** — Transitive but less informative

# Source Reference

Chapter 7: More Group Theory, Section 7.2, (7.2.1), p. 207.

# Verification Notes

- Definition source: Direct from (7.2.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
