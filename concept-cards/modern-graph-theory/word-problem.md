---
# === CORE IDENTIFICATION ===
concept: Word Problem for Groups
slug: word-problem

# === CLASSIFICATION ===
category: algebraic-graph-theory
subcategory: group-theory-basics
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 261
section: "VIII.1 Cayley and Schreier Diagrams"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - Dehn's word problem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-presentation
extends: []
related:
  - cayley-diagram
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the word problem for groups?"
---

# Quick Definition

The word problem asks whether two words in the generators of a finitely presented group represent the same group element. It is undecidable in general but solvable when the Cayley diagram can be constructed.

# Core Definition

Formulated by Max Dehn in 1911, the word problem asks for a general, effective method to decide in finitely many steps whether two given words represent the same group element (Bollobas, p. 261). The conjugacy problem and isomorphism problem are the other two fundamental problems. All three are undecidable in general, but solutions for specific presentations often use group diagrams.

# Prerequisites

- **Group presentation** -- The input framework

# Key Properties

1. Undecidable in general (a problem in logic)
2. Equivalent to deciding if a word equals the identity
3. Solved for a specific presentation if the Cayley diagram can be constructed
4. Explicit solutions are always based on specific presentations

# Construction / Recognition

## Connection to Cayley Diagrams
1. Construct the Cayley diagram of $A = \langle a, b, \ldots \mid R_\mu, \ldots \rangle$
2. Two words $W_1, W_2$ represent the same element iff walks from 1 corresponding to $W_1$ and $W_2$ end at the same vertex
3. If the construction terminates, the word problem is solved

# Context & Application

The word problem connects group theory to logic and computability. Dehn was a strong advocate of using group diagrams to solve specific instances. The undecidability in general is one of the deepest results connecting algebra and mathematical logic.

# Examples

**Example** (p. 260): In $A = \langle a, b \mid a^3b, b^3, a^4\rangle$: checking $aba^2b$ in $S_3$ by following the walk in the Cayley diagram yields $aba^2b = a^2$.

# Relationships

## Builds Upon
- **Group presentation** -- Input

## Enables
- Algorithmic group theory

## Related
- **Cayley diagram** -- Provides a solution when constructible

## Contrasts With
- None

# Common Errors

- **Error**: Assuming the word problem is always solvable
  **Correction**: It is undecidable in general; only specific presentations may have effective solutions

# Common Confusions

- **Confusion**: Thinking the word problem is about words in a language, not algebra
  **Clarification**: It concerns words (products) in group generators, not natural language

# Source Reference

Chapter VIII: Graphs, Groups and Matrices, Section VIII.1, page 261.

# Verification Notes

- Definition source: Direct from p. 261
- Confidence rationale: Explicit discussion
- Uncertainties: None
- Cross-reference status: Verified
