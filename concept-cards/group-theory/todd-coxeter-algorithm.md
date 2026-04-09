---
# === CORE IDENTIFICATION ===
concept: Todd-Coxeter Algorithm
slug: todd-coxeter-algorithm

# === CLASSIFICATION ===
category: group-actions
subcategory: computation
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Groups Acting on Sets"
chapter_number: 4
pdf_page: 69
section: "The Todd-Coxeter algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - coset enumeration

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - permutation-group
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can I enumerate cosets of a subgroup from a group presentation?"
---

# Quick Definition

The Todd-Coxeter algorithm computes the set of left cosets of a subgroup $H$ in a finitely presented group $G$, together with the action of $G$ on the cosets.

# Core Definition

"Let $G$ be a group described by a finite presentation, and let $H$ be a subgroup described by a generating set. Then the Todd-Coxeter algorithm is a strategy for writing down the set of left cosets of $H$ in $G$ together with the action of $G$ on the set" (Milne, p. 69).

# Prerequisites

- **Group action** — The algorithm constructs the action of $G$ on $G/H$
- **Permutation group** — The output is a permutation representation

# Key Properties

1. Rules: (i) each generator acts as a permutation, (ii) relations act trivially, (iii) generators of $H$ fix coset $1H$, (iv) the action is transitive
2. The algorithm introduces cosets as needed and identifies them when forced by the rules
3. When it terminates with a consistent table, it correctly describes the action (Artin 1991, 9.10)
4. It solves the problem of determining the order of a finite group from a presentation (use $H = 1$)
5. It does not solve the general problem of whether a presentation defines a finite group
6. Implemented in GAP

# Context & Application

The Todd-Coxeter algorithm is a practical computational tool for studying finitely presented groups. It produces explicit permutation representations.

# Examples

**Example 1** (pp. 69-71): For $G = \langle a, b, c \mid a^3, b^2, c^2, cba \rangle$ with $H = \langle c \rangle$, the algorithm finds three cosets with $a = (123)$, $b = (12)$, $c = (23)$, showing $G \simeq S_3$ and $H$ has order 2.

# Relationships

## Builds Upon
- **group-action**, **permutation-group**

# Source Reference

Chapter 4: Groups Acting on Sets, "The Todd-Coxeter algorithm", pages 69-71.

# Verification Notes

- Definition source: Direct from p. 69
- Confidence: HIGH — explicit description with worked example
- Uncertainties: None
