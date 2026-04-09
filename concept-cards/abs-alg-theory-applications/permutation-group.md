---
# === CORE IDENTIFICATION ===
concept: Permutation Group
slug: permutation-group

# === CLASSIFICATION ===
category: permutation-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Permutation Groups"
chapter_number: 5
pdf_page: 72
section: "5.1 Definitions and Notation"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetric-group
extends: []
related:
  - dihedral-group
  - alternating-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a permutation group?"
  - "How does a permutation group relate to a symmetric group?"
---

# Quick Definition

A permutation group is any subgroup of a symmetric group $S_n$. It is a group whose elements are permutations of a set, with composition as the group operation.

# Core Definition

"A subgroup of $S_n$ is called a permutation group" (Judson, p. 73). A permutation group consists of a subset of permutations of a set that is closed under composition, contains the identity, and contains inverses.

# Prerequisites

- **Symmetric Group** — A permutation group is defined as a subgroup of $S_n$

# Key Properties

1. Every permutation group is a subgroup of some $S_n$
2. The group operation is composition of permutations
3. By Cayley's theorem, every group is isomorphic to some permutation group
4. Permutation groups provide abundant examples of nonabelian groups

# Construction / Recognition

## To Construct:
1. Choose a subset of permutations from $S_n$
2. Verify closure under composition
3. Verify the identity permutation is included
4. Verify every element has its inverse in the set

## To Recognize:
1. Check that all elements are permutations of the same set
2. Verify the subset satisfies the group axioms under composition

# Context & Application

Permutation groups are central to the study of geometric symmetries and to Galois theory. They provide concrete representations of abstract groups.

# Examples

**Example 1** (p. 73): The subgroup $G = \{\text{id}, \sigma, \tau, \mu\}$ of $S_5$, where $\sigma = (45)$, $\tau = (13)$, $\mu = (13)(45)$, is a permutation group of order 4.

# Relationships

## Builds Upon
- **Symmetric Group** — A permutation group is a subgroup of $S_n$

## Enables
- **Cayley's Theorem** — Every group is isomorphic to a permutation group

## Related
- **Dihedral Group** — An important family of permutation groups
- **Alternating Group** — The subgroup of even permutations

# Common Errors

- **Error**: Assuming every permutation group contains all permutations of the set
  **Correction**: A permutation group is a *subgroup* and typically omits many permutations

# Common Confusions

- **Confusion**: Confusing "permutation group" with "symmetric group"
  **Clarification**: The symmetric group $S_n$ is the largest permutation group on $n$ letters; a permutation group is any subgroup of $S_n$

# Source Reference

Chapter 5: Permutation Groups, Section 5.1, page 73.

# Verification Notes

- Definition source: Direct quote from p. 73
- Confidence rationale: Explicit one-line definition
- Uncertainties: None
- Cross-reference status: Verified
